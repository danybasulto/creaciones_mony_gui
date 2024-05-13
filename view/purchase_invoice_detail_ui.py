import os
from controller.purchase_invoice_detail_controller import PurchaseInvoiceDetailController

class PurchaseInvoiceDetailUI:
    def __init__(self):
        self.purchase_invoice_detail_controller = PurchaseInvoiceDetailController()

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        while True:
            self.clear_console()
            print("--- Detalle de Factura de Compra ---")
            print("1. Crear Detalle de Factura de Compra")
            print("2. Eliminar Detalle de Factura de Compra")
            print("3. Salir")

            option = int(input('\nOpción: '))

            if option == 1:
                self.create_invoice_detail()
            elif option == 2:
                self.delete_invoice_detail()
            elif option == 3:
                break
            else:
                print('Opción no válida! Ingresa un número del 1 al 3.')

    def create_invoice_detail(self):
        self.clear_console()
        invoice_id = int(input('ID de la Factura de Compra: '))
        product_id = int(input('ID del producto: '))
        quantity = int(input('Cantidad: '))
        unit_price = float(input('Precio unitario: '))
        total_expense = float(input('Gasto total: '))
        self.purchase_invoice_detail_controller.create_invoice_detail(invoice_id, product_id, quantity, unit_price, total_expense)
        input('\nPresione ENTER para continuar...')

    def delete_invoice_detail(self):
        self.clear_console()
        detail_id = int(input('ID del Detalle de Factura de Compra a eliminar: '))
        self.purchase_invoice_detail_controller.delete_invoice_detail(detail_id)
        input('\nPresione ENTER para continuar...')
