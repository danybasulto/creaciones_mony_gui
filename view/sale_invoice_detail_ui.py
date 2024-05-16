import tkinter as tk
from tkinter import ttk, Entry, Label, messagebox, Text, END
from controller.sale_invoice_detail_controller import SalesInvoiceDetailController

class SaleInvoiceDetailUI:
    def __init__(self, root):
        self.root = root
        self.sales_invoice_detail_controller = SalesInvoiceDetailController()
        self.frame = None

        # Inicializar variables de cadena
        self.invoice_id_var = tk.StringVar()
        self.product_var = tk.StringVar()
        self.quantity_var = tk.StringVar()

    def go_back_to_menu(self):
        self.frame.pack_forget()
        self.root.menu()

    def clear_fields(self):
        self.invoice_id_var.set('')
        self.product_var.set('')
        self.quantity_var.set('')

    def create_invoice_detail(self):
        invoice_id = int(self.invoice_id_var.get())
        product_id = int(self.product_var.get().split(':')[0])  # Obtener solo el ID del producto seleccionado
        quantity = int(self.quantity_var.get())
        unit_price, total_income = self.sales_invoice_detail_controller.create_invoice_detail(invoice_id, product_id, quantity)
        if unit_price is not None and total_income is not None:
            messagebox.showinfo("Éxito", "Detalle de venta creado correctamente.")
            self.generate_receipt(invoice_id, product_id, quantity, unit_price, total_income)  # Generar el recibo
        else:
            messagebox.showerror("Error", "Error al crear el detalle de venta.")

    def generate_receipt(self, invoice_id, product_id, quantity, unit_price, total_income):
        # Obtener detalles adicionales para el recibo
        product_name, _ = self.sales_invoice_detail_controller.get_product_details(product_id)
        invoice_id = int(self.invoice_id_var.get())

        # Crear contenido del recibo
        receipt_content = f"*** Recibo de Venta ***\n\n"
        receipt_content += f"Factura de Venta: {invoice_id}\n"
        receipt_content += f"Producto: {product_name}\n"
        receipt_content += f"Cantidad: {quantity}\n"
        receipt_content += f"Precio Unitario: {unit_price}\n"
        receipt_content += f"Ingreso Total: {total_income}\n"

        # Mostrar el recibo en una ventana emergente
        receipt_window = tk.Toplevel()
        receipt_window.title("Recibo de Venta")
        receipt_text = Text(receipt_window, wrap="word", height=20, width=60)
        receipt_text.pack()
        receipt_text.insert(END, receipt_content)

    def start_gui(self):
        # Creación del marco principal y otros componentes...
        self.frame = ttk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        back_button = ttk.Button(self.frame, text="Menú Principal", command=self.go_back_to_menu)
        back_button.pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)

        Label(self.frame, text='ID de la Factura de Venta:').pack()
        invoice_combobox = ttk.Combobox(self.frame, textvariable=self.invoice_id_var, state='readonly')
        invoice_combobox.pack()
        invoice_combobox['values'] = self.sales_invoice_detail_controller.get_sales_invoices()

        Label(self.frame, text='Producto:').pack()
        product_combobox = ttk.Combobox(self.frame, textvariable=self.product_var, state='readonly')
        product_combobox.pack()
        products = self.sales_invoice_detail_controller.get_products()
        product_names = [f"{product[0]}: {product[1]}" for product in products]  # Concatenar ID y nombre del producto
        product_combobox['values'] = product_names

        Label(self.frame, text='Cantidad:').pack()
        Entry(self.frame, textvariable=self.quantity_var).pack()

        button_frame = ttk.Frame(self.frame)
        button_frame.pack()

        ttk.Button(button_frame, text='Generar Detalle de Venta', command=self.create_invoice_detail).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(button_frame, text='Limpiar campos', command=self.clear_fields).pack(side=tk.LEFT, padx=5, pady=5)

        return self.frame
