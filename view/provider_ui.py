import os

from controller.provider_controller import ProviderController

class ProviderUI:
    def __init__(self):
        self.provider_controller = ProviderController()
    
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def menu(self):
        while True:
            self.clear_console()
            print("--- Proveedores ---")
            print("1. Agregar Proveedor")
            print("2. Modificar Proveedor")
            print("3. Eliminar Proveedor")
            print("4. Mostrar Proveedores")
            print("5. Buscar Proveedor")
            print("6. Salir")
            
            option = int(input('\nOpción: '))
            
            if option == 1:
                self.create_provider()
            elif option == 2:
                self.update_provider()
            elif option == 3:
                self.delete_provider()
            elif option == 4:
                self.read_providers()
            elif option == 5:
                self.find_provider()
            elif option == 6:
                break
            else:
                print('Opción no válida! Ingresa un número del 1 al 6.')
    
    def create_provider(self):
        self.clear_console()
        
        bussiness_name = str(input('Nombre del negocio: '))
        contact_name = str(input('Nombre del contacto: '))
        address = str(input('Dirección: '))
        phone_number = int(input('Número de telefono: '))
        self.provider_controller.create(bussiness_name, contact_name, address, phone_number)
        input('\nPresione ENTER para continuar...')
        
    def read_providers(self):
        self.clear_console()
        self.provider_controller.read()
        input('\nPresione ENTER para continuar...')
        
    def update_provider(self):
        self.clear_console()
        # pedir el id a modificar
        id = int(input('ID del proveedor a modificar: '))
        # ingresar nuevos datos
        b_name = str(input('Nombre del negocio: '))
        c_name = str(input('Nombre del contacto: '))
        address = str(input('Dirección: '))
        phone_number = int(input('Número de telefono: '))
        # actualizar con los datos que ingreso el usuario
        self.provider_controller.update(id, b_name, c_name, address, phone_number)
        input('\nPresione ENTER para continuar...')
    
    def delete_provider(self):
        self.clear_console()
        id = int(input('ID del proveedor a eliminar: '))
        self.provider_controller.delete(id)
        input('\nPresione ENTER para continuar...')
    
    def find_provider(self):
        self.clear_console()
        b_name = str(input('Nombre del negocio: '))
        self.provider_controller.find(b_name)
        input('\nPresione ENTER para continuar...')