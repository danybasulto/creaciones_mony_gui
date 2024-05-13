import os

from view.product_ui import ProductoUI
from view.category_ui import CategoryUI
from view.customer_ui import CustomerUI
from view.provider_ui import ProviderUI
from view.sale_invoice_ui import SaleInvoiceUI
from view.sale_invoice_detail_ui import SaleInvoiceDetailUI
from view.purchase_invoice_ui import PurchaseInvoiceUI
from view.purchase_invoice_detail_ui import PurchaseInvoiceDetailUI

class App:
    def __init__(self):
        self.prod = ProductoUI()
        self.cat = CategoryUI()
        self.cus = CustomerUI()
        self.prov = ProviderUI()
        self.sale_inv = SaleInvoiceUI()
        self.sale_inv_d = SaleInvoiceDetailUI()
        self.pur_inv = PurchaseInvoiceUI()
        self.pur_inv_d = PurchaseInvoiceDetailUI()
        
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def menu(self):
        while True:
            self.clear_console()
            print("--- CREACIONES MONY ---")
            print("1. Productos")
            print("2. Categorias")
            print("3. Clientes")
            print("4. Proveedores")
            print("5. Factura Venta")
            print("6. Detalle Factura Venta")
            print("7. Factura Compra")
            print("8. Detalle Factura Compra")
            print("0. Salir")

            option = int(input('\nOpción: '))
                
            if option == 1:
                self.prod.menu()
            elif option == 2:
                self.cat.menu()
            elif option == 3:
                self.cus.menu()
            elif option == 4:
                self.prov.menu()
            elif option == 5:
                self.sale_inv.menu()
            elif option == 6:
                self.sale_inv_d.menu()
            elif option == 7:
                self.pur_inv.menu()
            elif option == 8:
                self.pur_inv_d.menu()
            elif option == 0:
                print('Gracias por usar el programa :)')
                break
            else:
                print('Opción no válida! Ingresa un número válido.')
