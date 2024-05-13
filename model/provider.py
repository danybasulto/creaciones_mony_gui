import psycopg2

from database.database import Database

class Provider:
    def __init__(self):
        # instancia de database para interactuar con la bd
        self.db = Database()
    
    def create(self, bn, cn, a, pn):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            query = """INSERT INTO Proveedor (
                nombre_negocio, nombre_contacto, direccion, no_celular) VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (bn, cn, a, pn))
            # cerrar conexion
            self.db.close_connection()
            print('\nProveedor agregado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al agregar proveedor: ', ex)
            
    def read(self):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            cursor.execute("SELECT * FROM Proveedor")
            # obtener columnas y asignar el valor a rows
            rows = cursor.fetchall()
            # cerrar conexion
            self.db.close_connection()
            
            if len(rows) == 0:
                print('No hay proveedores.')
            else:
                print('Proveedores:')
                for row in rows:
                    print(row)
        except psycopg2.Error as ex:
            print('Error al mostrar proveedores: ', ex)
    
    def update(self, id, bussiness_name, contact_name, address, phone_number):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            query = """UPDATE Proveedor SET nombre_negocio=%s,
            nombre_contacto=%s, direccion=%s, no_celular=%s WHERE id_proveedor=%s"""
            cursor.execute(query, (bussiness_name, contact_name, address, phone_number, id))
            self.db.connection.commit()
            # cerrar conexion
            self.db.close_connection()
            print('\nProveedor actualizado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al actualizar proveedor: ', ex)
    
    def delete(self, id):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            cursor.execute("DELETE FROM Proveedor WHERE id_proveedor=%s", (id,))
            self.db.connection.commit()
            # cerrar conexion
            self.db.close_connection()
            print('\nProveedor eliminado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al eliminar proveedor: ', ex)
    
    def find(self, bussines_name):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            cursor.execute("SELECT * FROM Proveedor WHERE nombre_negocio=%s", (bussines_name,))
            # obtener columnas y asignar el valor a rows
            rows = cursor.fetchall()
            # cerrar conexion
            self.db.close_connection()
            
            if len(rows) == 0:
                print('No hay negocios con ese nombre.')
            else:
                print('\nProveedores encontrados:')
                for row in rows:
                    print(row)
        except psycopg2.Error as ex:
            print('Error al buscar proveedor: ', ex)
    
    def get_provider(self):
        return self.fn, self.ln, self.a, self.pn