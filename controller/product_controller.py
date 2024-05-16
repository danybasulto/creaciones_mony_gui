import psycopg2
from model.product import Product
from database.database import Database

class ProductController:
    def __init__(self):
        self.producto = Product()
        self.db = Database()

    def create(self, nombre_categoria, nombre_producto, precio):
        id_categoria = self.producto.get_categoria_id(nombre_categoria)
        if id_categoria is not None:
            self.producto.create(id_categoria, nombre_producto, precio)
        else:
            print('La categoría especificada no existe.')

    def update(self, id_producto, nombre_categoria, nombre_producto, precio):
        id_categoria = self.producto.get_categoria_id(nombre_categoria)
        if id_categoria is not None:
            self.producto.update(id_producto, id_categoria, nombre_producto, precio)
        else:
            print('La categoría especificada no existe.')

    def read(self):
        products = self.producto.read()
        formatted_products = []
        for product in products:
            category_name = self.producto.get_category_name(product[2])
            if category_name is not None:
                formatted_products.append((product[0], product[1], category_name, product[3]))
            else:
                print('Error: No se pudo obtener el nombre de la categoría para el producto', product[0])
        return formatted_products

    '''def update(self, id_producto, nombre_categoria, nombre_producto, precio):
        id_categoria = self.producto.get_categoria_id(nombre_categoria)
        if id_categoria is not None:
            self.producto.update(id_producto, id_categoria, nombre_producto, precio)
        else:
            print('La categoría especificada no existe.')'''

    def delete(self, id_producto):
        self.producto.delete(id_producto)

    def find(self, nombre):
        self.producto.find(nombre)
        
    def get_categories(self):
        return self.producto.get_categories()
    