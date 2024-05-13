import os
from controller.product_controller import ProductController

class ProductoUI:
    def __init__(self):
        self.producto_controller = ProductController()
    
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def menu(self):
        while True:
            self.clear_console()
            print("--- Productos ---")
            print("1. Agregar Producto")
            print("2. Modificar Producto")
            print("3. Eliminar Producto")
            print("4. Mostrar Productos")
            print("5. Buscar Producto")
            print("6. Salir")
            
            option = int(input('\nOpción: '))
            
            if option == 1:
                self.create_producto()
            elif option == 2:
                self.update_producto()
            elif option == 3:
                self.delete_producto()
            elif option == 4:
                self.read_productos()
            elif option == 5:
                self.find_producto()
            elif option == 6:
                break
            else:
                print('Opción no válida! Ingresa un número del 1 al 6.')
    
    def create_producto(self):
        self.clear_console()
        
        nombre_categoria = str(input('Nombre de la categoría: '))
        nombre_producto = str(input('Nombre del producto: '))
        precio = float(input('Precio del producto: '))
        
        self.producto_controller.create(nombre_categoria, nombre_producto, precio)
        input('\nPresione ENTER para continuar...')
        
    def read_productos(self):
        self.clear_console()
        self.producto_controller.read()
        input('\nPresione ENTER para continuar...')
        
    def update_producto(self):
        self.clear_console()
        
        id_producto = int(input('ID del producto a modificar: '))
        nombre_categoria = str(input('Nombre de la nueva categoría: '))
        nombre_producto = str(input('Nuevo nombre del producto: '))
        precio = float(input('Nuevo precio del producto: '))
        
        self.producto_controller.update(id_producto, nombre_categoria, nombre_producto, precio)
        input('\nPresione ENTER para continuar...')
    
    def delete_producto(self):
        self.clear_console()
        id_producto = int(input('ID del producto a eliminar: '))
        self.producto_controller.delete(id_producto)
        input('\nPresione ENTER para continuar...')
    
    def find_producto(self):
        self.clear_console()
        nombre = str(input('Nombre del producto: '))
        self.producto_controller.find(nombre)
        input('\nPresione ENTER para continuar...')
