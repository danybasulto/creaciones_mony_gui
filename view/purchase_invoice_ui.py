import os
from controller.purchase_invoice_controller import PurchaseInvoiceController

class PurchaseInvoiceUI:
    def __init__(self):
        self.purchase_invoice_controller = PurchaseInvoiceController()

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        while True:
            self.clear_console()
            print("--- Factura de Compra ---")
            print("1. Crear Factura de Compra")
            print("2. Mostrar Facturas de Compra")
            print("3. Actualizar Factura de Compra")
            print("4. Eliminar Factura de Compra")
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
        supplier_id = int(input('ID del Proveedor: '))
        date = input('Fecha (YYYY-MM-DD): ')
        self.purchase_invoice_controller.create_invoice(supplier_id, date)
        input('\nPresione ENTER para continuar...')

    def read_invoices(self):
        self.clear_console()
        self.purchase_invoice_controller.read_invoices()
        input('\nPresione ENTER para continuar...')

    def update_invoice(self):
        self.clear_console()
        invoice_id = int(input('ID de la Factura de Compra a actualizar: '))
        supplier_id = int(input('ID del Proveedor: '))
        date = input('Fecha (YYYY-MM-DD): ')
        self.purchase_invoice_controller.update_invoice(invoice_id, supplier_id, date)
        input('\nPresione ENTER para continuar...')

    def delete_invoice(self):
        self.clear_console()
        invoice_id = int(input('ID de la Factura de Compra a eliminar: '))
        self.purchase_invoice_controller.delete_invoice(invoice_id)
        input('\nPresione ENTER para continuar...')
