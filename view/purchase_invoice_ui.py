import tkinter as tk
from tkinter import ttk, Entry, Label
from controller.purchase_invoice_controller import PurchaseInvoiceController

class PurchaseInvoiceUI:
    def __init__(self, root):
        self.root = root
        self.purchase_invoice_controller = PurchaseInvoiceController()
        self.frame = None
        
        # Inicializar variables de cadena
        self.supplier_id_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.invoice_id_var = tk.StringVar()

    def go_back_to_menu(self):
        self.hide()
        self.root.menu()

    def clear_fields(self):
        self.supplier_id_var.set('')
        self.date_var.set('')
        self.invoice_id_var.set('')

    def show_invoices(self):
        self.clear_fields()
        self.tree.delete(*self.tree.get_children())
        for invoice in self.purchase_invoice_controller.read_invoices():
            self.tree.insert('', 'end', text=invoice[0], values=(invoice[1], invoice[2]))

    def select_invoice(self, event):
        selected_items = self.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            values = self.tree.item(selected_item, 'values')
            self.invoice_id_var.set(self.tree.item(selected_item, 'text'))
            self.supplier_id_var.set(values[0])
            self.date_var.set(values[1])
        else:
            self.clear_fields()

    def create_invoice(self):
        supplier_id = int(self.supplier_id_var.get())
        date = self.date_var.get()
        self.purchase_invoice_controller.create_invoice(supplier_id, date)
        self.show_invoices()

    def update_invoice(self):
        invoice_id = int(self.invoice_id_var.get())
        supplier_id = int(self.supplier_id_var.get())
        date = self.date_var.get()
        self.purchase_invoice_controller.update_invoice(invoice_id, supplier_id, date)
        self.show_invoices()

    def delete_invoice(self):
        invoice_id = int(self.invoice_id_var.get())
        self.purchase_invoice_controller.delete_invoice(invoice_id)
        self.show_invoices()

    def show(self, root):
        self.root = root
        self.frame.pack(expand=True, fill=tk.BOTH)

    def hide(self):
        self.frame.pack_forget()

    def start_gui(self):
        # Creación del marco principal
        self.frame = ttk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Botón de regreso al menú principal
        back_button = ttk.Button(self.frame, text="Menú Principal", command=self.go_back_to_menu)
        back_button.pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)

        Label(self.frame, text='ID del Proveedor:').pack()  
        Entry(self.frame, textvariable=self.supplier_id_var).pack()  

        Label(self.frame, text='Fecha (YYYY-MM-DD):').pack()  
        Entry(self.frame, textvariable=self.date_var).pack()  

        button_frame = ttk.Frame(self.frame)  # Crear un marco para los botones
        button_frame.pack()  

        ttk.Button(button_frame, text='Crear Factura de Compra', command=self.create_invoice).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(button_frame, text='Mostrar Facturas de Compra', command=self.show_invoices).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(button_frame, text='Actualizar Factura de Compra', command=self.update_invoice).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(button_frame, text='Eliminar Factura de Compra', command=self.delete_invoice).pack(side=tk.LEFT, padx=5, pady=5)

        # Crear la tabla dentro del marco principal
        self.tree = ttk.Treeview(self.frame, columns=('ID Proveedor', 'Fecha'))
        self.tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)  
        self.tree.heading('#0', text='ID Factura')
        self.tree.heading('ID Proveedor', text='ID Proveedor')
        self.tree.heading('Fecha', text='Fecha')
        self.tree.bind('<ButtonRelease-1>', self.select_invoice)
        
        self.show_invoices()

        return self.frame
