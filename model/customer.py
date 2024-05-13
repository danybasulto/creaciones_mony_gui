import psycopg2

from database.database import Database

class Customer:
    def __init__(self):
        # instancia de database para interactuar con la bd
        self.db = Database()
    
    def create(self, fn, ln, a, pn):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            query = """INSERT INTO Cliente (
                nombre, apellido, direccion, no_celular) VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (fn, ln, a, pn))
            # cerrar conexion
            self.db.close_connection()
            print('\nCliente agregado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al agregar cliente: ', ex)
            
    def read(self):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            cursor.execute("SELECT * FROM Cliente")
            # obtener columnas y asignar el valor a rows
            rows = cursor.fetchall()
            # cerrar conexion
            self.db.close_connection()
            
            if len(rows) == 0:
                print('No hay clientes.')
            else:
                return rows
        except psycopg2.Error as ex:
            print('Error al mostrar clientes: ', ex)
    
    def update(self, id, first_name, last_name, address, phone_number):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            query = """UPDATE Cliente SET nombre=%s,
            apellido=%s, direccion=%s, no_celular=%s WHERE id_cliente=%s"""
            cursor.execute(query, (first_name, last_name, address, phone_number, id))
            self.db.connection.commit()
            # cerrar conexion
            self.db.close_connection()
            print('\nCliente actualizado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al actualizar cliente: ', ex)
    
    def delete(self, id):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            cursor.execute("DELETE FROM Cliente WHERE id_cliente=%s", (id,))
            self.db.connection.commit()
            # cerrar conexion
            self.db.close_connection()
            print('\nCliente eliminado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al eliminar cliente: ', ex)
    
    def find(self, first_name):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            cursor.execute("SELECT * FROM Cliente WHERE nombre=%s", (first_name,))
            # obtener columnas y asignar el valor a rows
            rows = cursor.fetchall()
            # cerrar conexion
            self.db.close_connection()
            
            if len(rows) == 0:
                print('No hay clientes con ese nombre.')
            else:
                print('\nClientes encontrados:')
                for row in rows:
                    print(row)
        except psycopg2.Error as ex:
            print('Error al buscar cliente: ', ex)
    
    def get_customer(self):
        return self.fn, self.ln, self.a, self.pn