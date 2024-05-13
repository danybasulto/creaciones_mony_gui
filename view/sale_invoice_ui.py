import os
from controller.sale_invoice_controller import SaleInvoiceController

class SaleInvoiceUI:
    def __init__(self):
        self.sale_invoice_controller = SaleInvoiceController()

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        while True:
            self.clear_console()
            print("--- Facturas de Venta ---")
            print("1. Crear Factura de Venta")
            print("2. Mostrar Facturas de Venta")
            print("3. Actualizar Factura de Venta")
            print("4. Eliminar Factura de Venta")
            print("5. Salir")

            option = int(input('\nOpción: '))

            if option == 1:
                self.create_invoice()
            elif option == 2:
                self.read_invoices()
            elif option == 3:
                self.update_invoice()
            elif option == 4:
                self.delete_invoice()
            elif option == 5:
                break
            else:
                print('Opción no válida! Ingresa un número del 1 al 5.')

    def create_invoice(self):
        self.clear_console()
        client_id = int(input('ID del cliente: '))
        date = input('Fecha (YYYY-MM-DD): ')
        self.sale_invoice_controller.create_invoice(client_id, date)
        input('\nPresione ENTER para continuar...')

    def read_invoices(self):
        self.clear_console()
        self.sale_invoice_controller.read_invoices()
        input('\nPresione ENTER para continuar...')

    def update_invoice(self):
        self.clear_console()
        invoice_id = int(input('ID de la Factura de Venta a actualizar: '))
        client_id = int(input('Nuevo ID del cliente: '))
        date = input('Nueva fecha (YYYY-MM-DD): ')
        self.sale_invoice_controller.update_invoice(invoice_id, client_id, date)
        input('\nPresione ENTER para continuar...')

    def delete_invoice(self):
        self.clear_console()
        invoice_id = int(input('ID de la Factura de Venta a eliminar: '))
        self.sale_invoice_controller.delete_invoice(invoice_id)
        input('\nPresione ENTER para continuar...')
