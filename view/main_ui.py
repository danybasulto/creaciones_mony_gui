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
        
        self.current_ui = None  # Almacena la instancia de la UI actual

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
            
        # Clientes
        btn_clientes = tk.Button(self, text="Clientes", command=self.create_customer_ui)
        btn_clientes.pack()
        # Proveedores
        btn_prov = tk.Button(self, text="Proveedores", command=self.create_providers_ui)
        btn_prov.pack()
        # categoria
        btn_categorias = tk.Button(self, text="Categorias", command=self.create_categories_ui)
        btn_categorias.pack()
        
        btn_purchase = tk.Button(self, text="Factura Compra", command=self.create_purchase_inv_ui)
        btn_purchase.pack()
        
        btn_purchase = tk.Button(self, text="Factura Venta", command=self.create_sale_inv_ui)
        btn_purchase.pack()

    def cargar_ui(self, ui_instance):
        # Limpia los campos de la interfaz de clientes antes de cargar otra interfaz
        if isinstance(self.current_ui, CustomerUI):
            self.current_ui.clear_fields()
        
        # Eliminar widgets actuales en la ventana principal
        for widget in self.winfo_children():
            widget.destroy()

        # Empaquetar el frame devuelto por start_gui() en la ventana principal
        frame = ui_instance.start_gui()
        frame.pack(expand=True, fill=tk.BOTH)
        
    def create_customer_ui(self):
        customer_ui = CustomerUI(self)
        self.cargar_ui(customer_ui)
    
    def create_categories_ui(self):
        cat_ui = CategoryUI(self)
        self.cargar_ui(cat_ui)
    
    def create_providers_ui(self):
        prov_ui = ProviderUI(self)
        self.cargar_ui(prov_ui)
    
    def create_purchase_inv_ui(self):
        purchase_ui = PurchaseInvoiceUI(self)
        self.cargar_ui(purchase_ui)
    
    def create_sale_inv_ui(self):
        sale_ui = SaleInvoiceUI(self)
        self.cargar_ui(sale_ui)