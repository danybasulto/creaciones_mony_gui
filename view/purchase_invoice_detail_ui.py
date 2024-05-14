import tkinter as tk
from tkinter import ttk, Entry, Label
from controller.purchase_invoice_detail_controller import PurchaseInvoiceDetailController

class PurchaseInvoiceDetailUI:
    def __init__(self, root):
        self.root = root
        self.purchase_invoice_detail_controller = PurchaseInvoiceDetailController()
        self.frame = None

        # Inicializar variables de cadena
        self.invoice_id_var = tk.StringVar()
        self.product_id_var = tk.StringVar()
        self.quantity_var = tk.StringVar()
        self.unit_price_var = tk.StringVar()
        self.total_expense_var = tk.StringVar()
        self.detail_id_var = tk.StringVar()

    def go_back_to_menu(self):
        self.hide()
        self.root.menu()

    def clear_fields(self):
        self.invoice_id_var.set('')
        self.product_id_var.set('')
        self.quantity_var.set('')
        self.unit_price_var.set('')
        self.total_expense_var.set('')
        self.detail_id_var.set('')

    def create_invoice_detail(self):
        invoice_id = int(self.invoice_id_var.get())
        product_id = int(self.product_id_var.get())
        quantity = int(self.quantity_var.get())
        unit_price = float(self.unit_price_var.get())
        total_expense = float(self.total_expense_var.get())
        self.purchase_invoice_detail_controller.create_invoice_detail(invoice_id, product_id, quantity, unit_price, total_expense)
        self.clear_fields()

    def delete_invoice_detail(self):
        detail_id = int(self.detail_id_var.get())
        self.purchase_invoice_detail_controller.delete_invoice_detail(detail_id)
        self.clear_fields()

    def show(self, root):
        self.root = root
        self.frame.pack(expand=True, fill=tk.BOTH)

    def hide(self):
        self.frame.pack_forget()

    def start_gui(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        back_button = ttk.Button(self.frame, text="Menú Principal", command=self.go_back_to_menu)
        back_button.pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)

        Label(self.frame, text='ID de la Factura de Compra:').pack()
        Entry(self.frame, textvariable=self.invoice_id_var).pack()

        Label(self.frame, text='ID del Producto:').pack()
        Entry(self.frame, textvariable=self.product_id_var).pack()

        Label(self.frame, text='Cantidad:').pack()
        Entry(self.frame, textvariable=self.quantity_var).pack()

        Label(self.frame, text='Precio Unitario:').pack()
        Entry(self.frame, textvariable=self.unit_price_var).pack()

        Label(self.frame, text='Total Gasto:').pack()
        Entry(self.frame, textvariable=self.total_expense_var).pack()

        Label(self.frame, text='ID del Detalle a Eliminar:').pack()
        Entry(self.frame, textvariable=self.detail_id_var).pack()

        button_frame = ttk.Frame(self.frame)
        button_frame.pack()

        ttk.Button(button_frame, text='Crear Detalle de Factura de Compra', command=self.create_invoice_detail).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(button_frame, text='Eliminar Detalle de Factura de Compra', command=self.delete_invoice_detail).pack(side=tk.LEFT, padx=5, pady=5)

        return self.frame
