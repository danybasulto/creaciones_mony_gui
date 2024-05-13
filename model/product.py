import psycopg2
from database.database import Database

class Product:
    def __init__(self):
        self.db = Database()
    
    def create(self, categoria, nombre, precio):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            query = """INSERT INTO Producto (categoria, nombre, precio) 
                       VALUES (%s, %s, %s)"""
            cursor.execute(query, (categoria, nombre, precio))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nProducto agregado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al agregar producto: ', ex)
            
    def read(self):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            cursor.execute("SELECT * FROM Producto")
            rows = cursor.fetchall()
            self.db.close_connection()
            
            if len(rows) == 0:
                print('No hay productos.')
            else:
                print('Productos:')
                for row in rows:
                    print(row)
        except psycopg2.Error as ex:
            print('Error al mostrar productos: ', ex)
    
    def update(self, id_producto, categoria, nombre, precio):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            query = """UPDATE Producto SET categoria=%s, nombre=%s, precio=%s 
                       WHERE id_producto=%s"""
            cursor.execute(query, (categoria, nombre, precio, id_producto))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nProducto actualizado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al actualizar producto: ', ex)
    
    def delete(self, id_producto):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            cursor.execute("DELETE FROM Producto WHERE id_producto=%s", (id_producto,))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nProducto eliminado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al eliminar producto: ', ex)
    
    def find(self, nombre):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            cursor.execute("SELECT * FROM Producto WHERE nombre=%s", (nombre,))
            rows = cursor.fetchall()
            self.db.close_connection()
            
            if len(rows) == 0:
                print('No hay productos con ese nombre.')
            else:
                print('\nProductos encontrados:')
                for row in rows:
                    print(row)
        except psycopg2.Error as ex:
            print('Error al buscar producto: ', ex)
