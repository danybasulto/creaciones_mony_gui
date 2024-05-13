import psycopg2

from database.database import Database

class Category:
    def __init__(self):
        # instancia de database para interactuar con la bd
        self.db = Database()
    
    def create(self, name):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            query = """INSERT INTO Categoria (
                nombre) VALUES (%s)"""
            cursor.execute(query, (name,))
            # cerrar conexion
            self.db.close_connection()
            print('\nCategoria agregada exitosamente.')
        except psycopg2.Error as ex:
            print('Error al agregar categoria: ', ex)
            
    def read(self):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            cursor.execute("SELECT * FROM Categoria")
            # obtener columnas y asignar el valor a rows
            rows = cursor.fetchall()
            # cerrar conexion
            self.db.close_connection()
            
            if len(rows) == 0:
                print('No hay categorias.')
            else:
                print('Categorias:')
                for row in rows:
                    print(row)
        except psycopg2.Error as ex:
            print('Error al mostrar categorias: ', ex)
    
    def update(self, id, name):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            cursor.execute("UPDATE Categoria SET nombre=%s WHERE id_categoria=%s", (name, id))
            self.db.connection.commit()
            # cerrar conexion
            self.db.close_connection()
            print('\nCategoria actualizada exitosamente.')
        except psycopg2.Error as ex:
            print('Error al actualizar categoria: ', ex)
    
    def delete(self, id):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            cursor.execute("DELETE FROM Categoria WHERE id_categoria=%s", (id,))
            self.db.connection.commit()
            # cerrar conexion
            self.db.close_connection()
            print('\nCategoria eliminado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al eliminar categoria: ', ex)
    
    def find(self, name):
        try:
            # establecer conexion a la base de datos
            self.db.connect()
            # crear cursor
            cursor = self.db.get_cursor()
            # ejecutar consulta
            cursor.execute("SELECT * FROM Categoria WHERE nombre=%s", (name,))
            # obtener columnas y asignar el valor a rows
            rows = cursor.fetchall()
            # cerrar conexion
            self.db.close_connection()
            
            if len(rows) == 0:
                print('No hay categorias con ese nombre.')
            else:
                print('\nCategorias encontradas:')
                for row in rows:
                    print(row)
        except psycopg2.Error as ex:
            print('Error al buscar categoria: ', ex)
    
    def get_category(self):
        return self.fn, self.ln, self.a, self.pn