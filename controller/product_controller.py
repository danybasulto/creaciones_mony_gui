import psycopg2
from model.product import Product
from database.database import Database

class ProductController:
    def __init__(self):
        self.producto = Product()
        self.db = Database()

    def create(self, nombre_categoria, nombre_producto, precio):
        id_categoria = self.get_categoria_id(nombre_categoria)
        if id_categoria is not None:
            self.producto.create(id_categoria, nombre_producto, precio)
        else:
            print('La categoría especificada no existe.')
        
    def read(self):
        return self.producto.read()

    def update(self, id_producto, nombre_categoria, nombre_producto, precio):
        id_categoria = self.get_categoria_id(nombre_categoria)
        if id_categoria is not None:
            self.producto.update(id_producto, id_categoria, nombre_producto, precio)
        else:
            print('La categoría especificada no existe.')

    def delete(self, id_producto):
        self.producto.delete(id_producto)

    def find(self, nombre):
        self.producto.find(nombre)

    def get_categoria_id(self, nombre_categoria):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            query = "SELECT id_categoria FROM Categoria WHERE nombre = %s"
            cursor.execute(query, (nombre_categoria,))
            result = cursor.fetchone()
            self.db.close_connection()
            if result:
                return result[0]
            else:
                return None
        except psycopg2.Error as ex:
            print('Error al obtener el ID de la categoría: ', ex)
            return None
