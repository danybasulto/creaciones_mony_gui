import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

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
        self.geometry("1080x720")
        self.configure(background='#fcfcd7')
        # icono ventana
        self.iconbitmap('./images/icono.ico')
        # imagen negocio
        self.img = None
        
        self.current_ui = None  # Almacena la instancia de la UI actual

        self.menu()

    def menu(self):
        # Barra de menú
        barra_menu = tk.Menu(self)
        self.config(menu=barra_menu)
        
        # Etiqueta de título
        label_titulo = tk.Label(self, text='CREACIONES MONY', bg='#fcfcd7', fg='#f04158')
        label_titulo.config(font=('Roboto', 25, 'bold'))
        label_titulo.pack(pady=20)
        
        # imagen
        self.img = Image.open('./images/logo-mony.png')
        self.img = self.img.resize((300, 300), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        lbl_img = tk.Label(self, image=self.img, borderwidth=10, highlightbackground='#f04158')
        lbl_img.image = self.img
        lbl_img.pack(pady=20)
        
        # Botones
        btn_product = tk.Button(self, text="Productos", bg='#f1db42', command=self.create_product_ui)
        btn_product.place(x=350,y=450)
        
        btn_categorias = tk.Button(self, text="Categorias", bg='#f1db42', command=self.create_categories_ui)
        btn_categorias.place(x=450,y=450)
        
        btn_clientes = tk.Button(self, text="Clientes", bg='#f1db42', command=self.create_customer_ui)
        btn_clientes.place(x=550,y=450)
        
        btn_prov = tk.Button(self, text="Proveedores", bg='#f1db42', command=self.create_providers_ui)
        btn_prov.place(x=650,y=450)
        
        btn_purchase = tk.Button(self, text="Factura Compra", bg='#f04158', command=self.create_purchase_inv_ui)
        btn_purchase.place(x=220,y=250)
        
        btn_purchase_det = tk.Button(self, text="Detalle Factura Compra", bg='#f04158', command=self.create_purchase_inv_det_ui)
        btn_purchase_det.place(x=200,y=300)
        
        btn_sale = tk.Button(self, text="Factura Venta", bg='#67be9b', command=self.create_sale_inv_ui)
        btn_sale.place(x=770,y=250)
        
        btn_sale_det = tk.Button(self, text="Detalle Factura Venta", bg='#67be9b', command=self.create_sale_inv_det_ui)
        btn_sale_det.place(x=750,y=300)

    def cargar_ui(self, ui_instance):
        # Limpia los campos de la interfaz de clientes antes de cargar otra interfaz
        #if isinstance(self.current_ui, CustomerUI):
        #    self.current_ui.clear_fields()
        
        # Eliminar widgets actuales en la ventana principal
        for widget in self.winfo_children():
            widget.destroy()

        # Empaquetar el frame devuelto por start_gui() en la ventana principal
        frame = ui_instance.start_gui()
        frame.pack(expand=True, fill=tk.BOTH)
        
    def create_product_ui(self):
        pro_ui = ProductUI(self)
        self.cargar_ui(pro_ui)
    
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
        
    def create_purchase_inv_det_ui(self):
        purchase_ui = PurchaseInvoiceDetailUI(self)
        self.cargar_ui(purchase_ui)
    
    def create_sale_inv_det_ui(self):
        sale_ui = SaleInvoiceDetailUI(self)
        self.cargar_ui(sale_ui)