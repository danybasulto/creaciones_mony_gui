import tkinter as tk
from tkinter import ttk, messagebox
from controller.product_controller import ProductController

class ProductUI:
    def __init__(self):
        self.product_controller = ProductController()

    def clear_fields(self):
        self.id_var.set('')
        self.nombre_categoria_var.set('')
        self.nombre_producto_var.set('')
        self.precio_var.set('')

    def show_products(self):
        self.clear_fields()
        products = self.product_controller.read()
        self.tree.delete(*self.tree.get_children())
        for product in products:
            self.tree.insert('', 'end', text=product[0], values=(product[1], product[2], product[3]))

    def select_product(self, event):
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, 'values')
        self.id_var.set(self.tree.item(selected_item, 'text'))
        self.nombre_categoria_var.set(values[0])
        self.nombre_producto_var.set(values[1])
        self.precio_var.set(values[2])

    def create_product(self):
        nombre_categoria = self.nombre_categoria_var.get()
        nombre_producto = self.nombre_producto_var.get()
        precio = float(self.precio_var.get())
        self.product_controller.create(nombre_categoria, nombre_producto, precio)
        self.show_products()
        messagebox.showinfo("Éxito", "Producto creado correctamente.")

    def update_product(self):
        product_id = self.id_var.get()
        nombre_categoria = self.nombre_categoria_var.get()
        nombre_producto = self.nombre_producto_var.get()
        precio = float(self.precio_var.get())
        self.product_controller.update(product_id, nombre_categoria, nombre_producto, precio)
        self.show_products()
        messagebox.showinfo("Éxito", "Producto actualizado correctamente.")

    def delete_product(self):
        product_id = self.id_var.get()
        self.product_controller.delete(product_id)
        self.show_products()
        messagebox.showinfo("Éxito", "Producto eliminado correctamente.")

    def start_gui(self):
        root = tk.Tk()
        root.title('Gestión de Productos')

        self.id_var = tk.StringVar()
        self.nombre_categoria_var = tk.StringVar()
        self.nombre_producto_var = tk.StringVar()
        self.precio_var = tk.StringVar()

        frame = ttk.Frame(root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(frame, text='ID:').grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(frame, textvariable=self.id_var, state='readonly').grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text='Nombre Categoría:').grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(frame, textvariable=self.nombre_categoria_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text='Nombre Producto:').grid(row=2, column=0, padx=5, pady=5)
        ttk.Entry(frame, textvariable=self.nombre_producto_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text='Precio:').grid(row=3, column=0, padx=5, pady=5)
        ttk.Entry(frame, textvariable=self.precio_var).grid(row=3, column=1, padx=5, pady=5)

        btn_frame = ttk.Frame(root)
        btn_frame.grid(row=1, column=0, padx=10, pady=10)

        ttk.Button(btn_frame, text='Agregar Producto', command=self.create_product).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text='Modificar Producto', command=self.update_product).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text='Eliminar Producto', command=self.delete_product).grid(row=0, column=2, padx=5, pady=5)

        self.tree = ttk.Treeview(root, columns=('Nombre Categoría', 'Nombre Producto', 'Precio'))
        self.tree.grid(row=2, column=0, padx=10, pady=10)
        self.tree.heading('#0', text='ID')
        self.tree.heading('Nombre Categoría', text='Nombre Categoría')
        self.tree.heading('Nombre Producto', text='Nombre Producto')
        self.tree.heading('Precio', text='Precio')
        self.tree.bind('<ButtonRelease-1>', self.select_product)

        self.show_products()
        
        root.mainloop()
