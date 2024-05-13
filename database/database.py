import psycopg2
import configparser
import subprocess

from database.constants import *

class Database:
    def __init__(self, credentials=CONFIG_FILE):
        self.config = self.read_config(credentials)
        self.connection = None
    
    def read_config(self, credentials):
        # crear instancia ConfigParser
        config = configparser.ConfigParser()
        # leer archivo
        config.read(credentials)
        #print(config.sections())###
        return config['postgresql']
    
    def connect(self):
        try:
            # establecer conexion a postgres
            self.connection = psycopg2.connect(**self.config)
            # evitar que se inicie una transaccion automaticamente
            self.connection.autocommit = True
            # comprobar conexion
            #print('Conexion exitosa!')
        except psycopg2.Error as ex:
            print('Error al conectar a la bd: ', ex)
            
    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            #print('Conexion cerrada.')
            
    def check_connection(self):
        if self.connection is not None:
            self.close_connection()
            self.connect()
    
    def get_cursor(self):
        if self.connection is None:
            # mostrar excepcion de tipo ValueError
            raise ValueError('No hay conexion establecida.')
        # retornar cursor para realizar operaciones en la bd
        return self.connection.cursor()
    
    def execute_query(self, query):
        # crear cursor
        cursor = self.get_cursor()
        # ejecutar consulta
        cursor.execute(query)
        # cerrar conexion
        cursor.close()
    
    def backup_db(self):
        try:
            self.connect()
            # ejecutar respaldo usando pg_dump
            subprocess.run(['pg_dump',
                            '-h', self.config['host'],
                            '-U', self.config['user'],
                            '-d', self.config['database'],
                            '-f', BACKUP_FILE])
            print('Base de datos respaldada con éxito.')
        except psycopg2.Error as ex:
            print('Ocurrió un error al respaldar la base de datos: ', ex)
        finally:
            self.close_connection()
    
    def restore_db(self):
        try:
            self.connect()
            # eliminar la base de datos actual
            self.execute_query(f"DROP DATABASE IF EXISTS {self.config['database']}")
            # crear la nueva base de datos
            self.execute_query(f"CREATE DATABASE {self.config['database']}")
            # restaurar la bd desde el respaldo
            subprocess.run(['psql',
                            '-h', self.config['host'],
                            '-U', self.config['user'],
                            '-d', self.config['database'],
                            '-f', BACKUP_FILE])
            print('Base de datos restaurada éxitosamente.')
        except psycopg2.Error as ex:
            print('Ocurrió un error al restaurar la base de datos: ', ex)
        finally:
            self.close_connection()
    
    def create_tables(self):
        try:
            self.connect()
            # crear tablas
            self.execute_query(TABLE_CATEGORIA)
            self.execute_query(TABLE_PRODUCTO)
            self.execute_query(TABLE_CLIENTE)
            self.execute_query(TABLE_FACTURA_VENTA)
            self.execute_query(TABLE_DETALLE_F_VENTA)
            self.execute_query(TABLE_PROVEEDOR)
            self.execute_query(TABLE_FACTURA_COMPRA)
            self.execute_query(TABLE_DETALLE_F_COMPRA)
            print('Tablas creadas exitosamente.')
        except psycopg2.Error as ex:
            print('Error al crear las tablas: ', ex)
        finally:
            self.close_connection()

    def crear_trigger_venta(self):
        try:
            self.connect()
            cursor = self.get_cursor()
            cursor.execute("""
                CREATE OR REPLACE FUNCTION actualizar_cantidad_stock_venta()
                RETURNS TRIGGER AS $$
                BEGIN
                    UPDATE Producto
                    SET cantidad_stock = cantidad_stock - NEW.cantidad
                    WHERE id_producto = NEW.producto;
                    RETURN NEW;
                END;
                $$ LANGUAGE plpgsql;
                
                CREATE TRIGGER actualizar_stock_venta
                AFTER INSERT ON Detalle_F_Venta
                FOR EACH ROW
                EXECUTE FUNCTION actualizar_cantidad_stock_venta();
            """)
            print("TRIGGER para ventas creado exitosamente.")
        except psycopg2.Error as ex:
            print("Error al crear el TRIGGER para ventas:", ex)
        finally:
            if cursor:
                cursor.close()
                self.close_connection()

    def crear_trigger_compra(self):
        try:
            self.connect()
            cursor = self.get_cursor()
            cursor.execute("""
                CREATE OR REPLACE FUNCTION actualizar_cantidad_stock_compra()
                RETURNS TRIGGER AS $$
                BEGIN
                    UPDATE Producto
                    SET cantidad_stock = cantidad_stock + NEW.cantidad
                    WHERE id_producto = NEW.producto;
                    RETURN NEW;
                END;
                $$ LANGUAGE plpgsql;
                
                CREATE TRIGGER actualizar_stock_compra
                AFTER INSERT ON Detalle_F_Compra
                FOR EACH ROW
                EXECUTE FUNCTION actualizar_cantidad_stock_compra();
            """)
            print("TRIGGER para compras creado exitosamente.")
        except psycopg2.Error as ex:
            print("Error al crear el TRIGGER para compras:", ex)
        finally:
            if cursor:
                cursor.close()
                self.close_connection()
    
    def create_functions(self):
        functions = [
            """
            CREATE OR REPLACE FUNCTION obtener_articulos_vendidos_cliente(cliente_id INT) RETURNS TABLE (
                nombre_producto VARCHAR(50),
                cantidad_vendida INT
            ) AS $$
            BEGIN
                RETURN QUERY 
                SELECT p.nombre, dfv.cantidad
                FROM Detalle_F_Venta dfv
                JOIN Producto p ON dfv.producto = p.id_producto
                WHERE dfv.folio_venta IN (
                    SELECT folio_venta 
                    FROM Factura_Venta 
                    WHERE cliente = cliente_id
                );
            END $$ LANGUAGE plpgsql;
            """,
            """
            CREATE OR REPLACE FUNCTION obtener_articulos_comprados_proveedor(proveedor_id INT) RETURNS TABLE (
                nombre_producto VARCHAR(50),
                cantidad_comprada INT
            ) AS $$
            BEGIN
                RETURN QUERY 
                SELECT p.nombre, dfc.cantidad
                FROM Detalle_F_Compra dfc
                JOIN Producto p ON dfc.producto = p.id_producto
                WHERE dfc.folio_compra IN (
                    SELECT folio_compra 
                    FROM Factura_Compra 
                    WHERE proveedor = proveedor_id
                );
            END $$ LANGUAGE plpgsql;
            """,
            # más definiciones de funciones aquí
        ]
        for function in functions:
            self.execute_query(function)

    def create_procedures(self):
        procedures = [
            """
            CREATE OR REPLACE PROCEDURE crearCliente(IdCliente INT, nombre VARCHAR(50))
            AS $$
            BEGIN
                INSERT INTO Cliente(codigo_cliente, nombre) VALUES (IdCliente, nombre);
            END;
            $$ LANGUAGE plpgsql;
            """,
            """
            CREATE OR REPLACE PROCEDURE crearVenta(cliente_id INT, producto_id INT, cantidad INT)
            AS $$
            BEGIN
                INSERT INTO Factura_Venta(cliente, fecha) VALUES (cliente_id, NOW());
                INSERT INTO Detalle_F_Venta(folio_venta, producto, cantidad, precio_venta, ingreso_total)
                VALUES ((SELECT MAX(folio_venta) FROM Factura_Venta), producto_id, cantidad,
                (SELECT precio FROM Producto WHERE id_producto = producto_id), cantidad * (SELECT precio FROM Producto WHERE id_producto = producto_id));
            END;
            $$ LANGUAGE plpgsql;
            """,
            # más definiciones de procedimientos almacenados aquí
        ]
        for procedure in procedures:
            self.execute_query(procedure)
    
    def create_views(self):
        views = [
            """
            CREATE OR REPLACE VIEW vista_clientes_venta AS 
            SELECT c.nombre AS nombre_cliente, dfv.cantidad, p.nombre AS nombre_producto
            FROM Cliente c
            JOIN Factura_Venta fv ON c.id_cliente = fv.cliente
            JOIN Detalle_F_Venta dfv ON fv.folio_venta = dfv.folio_venta
            JOIN Producto p ON dfv.producto = p.id_producto;
            """,
            """
            CREATE OR REPLACE VIEW vista_proveedores_compra AS 
            SELECT pr.nombre_negocio AS nombre_proveedor, dfc.cantidad, p.nombre AS nombre_producto
            FROM Proveedor pr
            JOIN Factura_Compra fc ON pr.id_proveedor = fc.proveedor
            JOIN Detalle_F_Compra dfc ON fc.folio_compra = dfc.folio_compra
            JOIN Producto p ON dfc.producto = p.id_producto;
            """,
            # más definiciones de vistas aquí
        ]
        for view in views:
            self.execute_query(view)

#db = Database()
#db.connect()
#db.create_tables()
#db.crear_trigger_venta()
#db.crear_trigger_compra()
#db.create_functions()
#db.create_procedures()
#db.create_views()
