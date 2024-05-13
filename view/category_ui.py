import os

from controller.category_controller import CategoryController

class CategoryUI:
    def __init__(self):
        self.category_controller = CategoryController()
    
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def menu(self):
        while True:
            self.clear_console()
            print("--- Categorías ---")
            print("1. Agregar Categoría")
            print("2. Modificar Categoría")
            print("3. Eliminar Categoría")
            print("4. Mostrar Categorías")
            print("5. Buscar Categoría")
            print("6. Salir")
            
            option = int(input('\nOpción: '))
            
            if option == 1:
                self.create_category()
            elif option == 2:
                self.update_category()
            elif option == 3:
                self.delete_category()
            elif option == 4:
                self.read_categories()
            elif option == 5:
                self.find_category()
            elif option == 6:
                break
            else:
                print('Opción no válida! Ingresa un número del 1 al 6.')
    
    def create_category(self):
        self.clear_console()
        
        name = str(input('Nombre: '))
        self.category_controller.create(name)
        input('\nPresione ENTER para continuar...')
        
    def read_categories(self):
        self.clear_console()
        self.category_controller.read()
        input('\nPresione ENTER para continuar...')
        
    def update_category(self):
        self.clear_console()
        # pedir el id a modificar
        id = int(input('ID de la categoría a modificar: '))
        # ingresar nuevos datos
        name = str(input('Nombre: '))
        # actualizar categoria con los datos que ingreso el usuario
        self.category_controller.update(id, name)
        input('\nPresione ENTER para continuar...')
    
    def delete_category(self):
        self.clear_console()
        id = int(input('ID de la categoría a eliminar: '))
        self.category_controller.delete(id)
        input('\nPresione ENTER para continuar...')
    
    def find_category(self):
        self.clear_console()
        name = str(input('Nombre: '))
        self.category_controller.find(name)
        input('\nPresione ENTER para continuar...')