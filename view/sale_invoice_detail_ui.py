import os
from controller.sale_invoice_detail_controller import SaleInvoiceDetailController

class SaleInvoiceDetailUI:
    def __init__(self):
        self.sale_invoice_detail_controller = SaleInvoiceDetailController()

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        while True:
            self.clear_console()
            print("--- Detalle de Factura de Venta ---")
            print("1. Crear Detalle de Factura de Venta")
            print("2. Eliminar Detalle de Factura de Venta")
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
        invoice_id = int(input('ID de la Factura de Venta: '))
        product_id = int(input('ID del producto: '))
        quantity = int(input('Cantidad: '))
        unit_price = float(input('Precio unitario: '))
        total_income = float(input('Ingreso total: '))
        self.sale_invoice_detail_controller.create_invoice_detail(invoice_id, product_id, quantity, unit_price, total_income)
        input('\nPresione ENTER para continuar...')

    def delete_invoice_detail(self):
        self.clear_console()
        detail_id = int(input('ID del Detalle de Factura de Venta a eliminar: '))
        self.sale_invoice_detail_controller.delete_invoice_detail(detail_id)
        input('\nPresione ENTER para continuar...')
