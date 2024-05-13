import tkinter as tk
from tkinter import font

from view.product_ui import ProductUI
from view.category_ui import CategoryUI
from view.customer_ui import CustomerUI
from view.provider_ui import ProviderUI
from view.sale_invoice_ui import SaleInvoiceUI
from view.sale_invoice_detail_ui import SaleInvoiceDetailUI
from view.purchase_invoice_ui import PurchaseInvoiceUI
from view.purchase_invoice_detail_ui import PurchaseInvoiceDetailUI

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CREACIONES MONY")
        self.geometry("800x600")
        
        self.prod_ui = ProductUI()
        self.cat_ui = CategoryUI()
        self.prov_ui = ProviderUI()
        self.sale_inv_ui = SaleInvoiceUI()
        self.sale_inv_d_ui = SaleInvoiceDetailUI()
        self.pur_inv_ui = PurchaseInvoiceUI()
        self.pur_inv_d_ui = PurchaseInvoiceDetailUI()
        
        self.menu()

    def menu(self):
        font_awesome = font.Font(family='FontAwesome', size=12)
        
        # Barra de menú
        barra_menu = tk.Menu(self)
        self.config(menu=barra_menu)
        
        # Etiqueta de título
        label_titulo = tk.Label(self, text='CREACIONES MONY')
        label_titulo.config(font=('Roboto', 15))
        label_titulo.pack(pady=20)
        
        # Opciones del menú
        opciones = [
            ("Productos", lambda: self.cargar_ui(self.prod_ui)),
            ("Categorías", lambda: self.cargar_ui(self.cat_ui)),
            ("Clientes", lambda: self.cargar_ui(CustomerUI(self, self.menu))),  
            ("Proveedores", lambda: self.cargar_ui(self.prov_ui)),
            ("Factura Venta", lambda: self.cargar_ui(self.sale_inv_ui)),
            ("Detalle Factura Venta", lambda: self.cargar_ui(self.sale_inv_d_ui)),
            ("Factura Compra", lambda: self.cargar_ui(self.pur_inv_ui)),
            ("Detalle Factura Compra", lambda: self.cargar_ui(self.pur_inv_d_ui)),
        ]
        
        # Botones de opciones
        for nombre, comando in opciones:
            boton = tk.Button(self, text=nombre, command=comando)
            boton.pack()
        
        # Botón de salir
        boton_salir = tk.Button(self, text="Salir", command=self.salir)
        boton_salir.pack(pady=20)
    
    def cargar_ui(self, ui_instance):
        # Eliminar widgets actuales en la ventana principal
        for widget in self.winfo_children():
            widget.destroy()

        # Empaquetar el frame devuelto por start_gui() en la ventana principal
        frame = ui_instance.start_gui()
        frame.pack(expand=True, fill=tk.BOTH)
        
    def salir(self):
        print('Gracias por usar el programa :)')
        self.destroy()
