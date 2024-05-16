import tkinter as tk
from tkinter import ttk, Entry, Label, messagebox, Text, END
from controller.purchase_invoice_detail_controller import PurchaseInvoiceDetailController

class PurchaseInvoiceDetailUI:
    def __init__(self, root):
        self.root = root
        self.purchase_invoice_detail_controller = PurchaseInvoiceDetailController()
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
        unit_price, total_expense = self.purchase_invoice_detail_controller.create_invoice_detail(invoice_id, product_id, quantity)
        if unit_price is not None and total_expense is not None:
            messagebox.showinfo("Éxito", "Detalle de compra creado correctamente.")
            self.generate_ticket(invoice_id, product_id, quantity, unit_price, total_expense)  # Generar el ticket
        else:
            messagebox.showerror("Error", "Error al crear el detalle de compra.")

    def generate_ticket(self, invoice_id, product_id, quantity, unit_price, total_expense):
        # Obtener detalles adicionales para el ticket
        product_name, _ = self.purchase_invoice_detail_controller.get_product_details(product_id)
        invoice_id = int(self.invoice_id_var.get())

        # Crear contenido del ticket
        ticket_content = f"*** Ticket de Compra ***\n\n"
        ticket_content += f"Factura de Compra: {invoice_id}\n"
        ticket_content += f"Producto: {product_name}\n"
        ticket_content += f"Cantidad: {quantity}\n"
        ticket_content += f"Precio Unitario: {unit_price}\n"
        ticket_content += f"Gasto Total: {total_expense}\n"

        # Mostrar el ticket en una ventana emergente
        ticket_window = tk.Toplevel()
        ticket_window.title("Ticket de Compra")
        ticket_text = Text(ticket_window, wrap="word", height=20, width=60)
        ticket_text.pack()
        ticket_text.insert(END, ticket_content)

    def start_gui(self):
        # Creación del marco principal y otros componentes...
        self.frame = ttk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        back_button = ttk.Button(self.frame, text="Menú Principal", command=self.go_back_to_menu)
        back_button.pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)

        Label(self.frame, text='ID de la Factura de Compra:').pack()
        invoice_combobox = ttk.Combobox(self.frame, textvariable=self.invoice_id_var, state='readonly')
        invoice_combobox.pack()
        invoice_combobox['values'] = self.purchase_invoice_detail_controller.get_purchase_invoices()

        Label(self.frame, text='Producto:').pack()
        product_combobox = ttk.Combobox(self.frame, textvariable=self.product_var, state='readonly')
        product_combobox.pack()
        products = self.purchase_invoice_detail_controller.get_products()
        product_names = [f"{product[0]}: {product[1]}" for product in products]  # Concatenar ID y nombre del producto
        product_combobox['values'] = product_names

        Label(self.frame, text='Cantidad:').pack()
        Entry(self.frame, textvariable=self.quantity_var).pack()

        button_frame = ttk.Frame(self.frame)
        button_frame.pack()

        ttk.Button(button_frame, text='Generar Detalle de Compra', command=self.create_invoice_detail).pack(side=tk.LEFT, padx=5, pady=5)

        return self.frame
