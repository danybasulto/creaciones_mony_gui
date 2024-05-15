import tkinter as tk
from tkinter import ttk, messagebox
from controller.product_controller import ProductController

class ProductUI:
    def __init__(self, root):
        self.root = root
        self.product_controller = ProductController()
        self.frame = None
        
        # Inicializar variables de cadena
        self.id_var = tk.StringVar()
        self.nombre_producto_var = tk.StringVar()
        self.precio_var = tk.StringVar()
        self.selected_category = tk.StringVar()  # Variable para almacenar la categoría seleccionada

    def clear_fields(self):
        self.id_var.set('')
        self.nombre_producto_var.set('')
        self.precio_var.set('')

    def show_products(self):
        self.clear_fields()
        products = self.product_controller.read()
        self.tree.delete(*self.tree.get_children())
        for product in products:
            self.tree.insert('', 'end', text=product[0], values=(product[1], product[2], product[3]))

    def select_product(self, event):
        if self.tree.selection():
            selected_item = self.tree.selection()[0]
            values = self.tree.item(selected_item, 'values')
            if values:
                self.id_var.set(self.tree.item(selected_item, 'text'))
                product_id = self.tree.item(selected_item, 'text')
                self.nombre_producto_var.set(values[0])
                category_id = self.product_controller.producto.get_categoria_id(values[1])
                if category_id is not None:
                    self.selected_category.set(category_id)
                else:
                    print('Error: No se pudo obtener el nombre de la categoría.')
                self.precio_var.set(values[2])

    def create_product(self):
        nombre_producto = self.nombre_producto_var.get()
        precio = float(self.precio_var.get())
        nombre_categoria = self.selected_category.get()  # Obtener la categoría seleccionada
        self.product_controller.create(nombre_categoria, nombre_producto, precio)
        self.show_products()  # Añadir esta línea para actualizar la tabla
        messagebox.showinfo("Éxito", "Producto creado correctamente.")

    def update_product(self):
        product_id = self.id_var.get()
        nombre_producto = self.nombre_producto_var.get()
        precio = float(self.precio_var.get())
        nombre_categoria = self.selected_category.get()  # Obtener la categoría seleccionada
        self.product_controller.update(product_id, nombre_categoria, nombre_producto, precio)
        self.show_products()
        messagebox.showinfo("Éxito", "Producto actualizado correctamente.")

    def delete_product(self):
        product_id = self.id_var.get()
        self.product_controller.delete(product_id)
        self.show_products()
        messagebox.showinfo("Éxito", "Producto eliminado correctamente.")

    def start_gui(self):
        # Creación del marco principal
        self.frame = ttk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        ttk.Label(self.frame, text='Nombre:').pack()  
        ttk.Entry(self.frame, textvariable=self.nombre_producto_var).pack()  

        ttk.Label(self.frame, text='Categoría:').pack()  
        # Combobox para seleccionar la categoría
        self.category_combobox = ttk.Combobox(self.frame, textvariable=self.selected_category, state='readonly')
        self.category_combobox.pack()
        self.category_combobox['values'] = self.product_controller.get_categories()

        ttk.Label(self.frame, text='Precio:').pack() 
        ttk.Entry(self.frame, textvariable=self.precio_var).pack()  

        btn_frame = ttk.Frame(self.frame)  # Crear un marco para los botones
        btn_frame.pack()  

        ttk.Button(btn_frame, text='Agregar', command=self.create_product).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(btn_frame, text='Modificar', command=self.update_product).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(btn_frame, text='Eliminar', command=self.delete_product).pack(side=tk.LEFT, padx=5, pady=5)  

        # Crear la tabla dentro del marco principal
        self.tree = ttk.Treeview(self.frame, columns=('Producto', 'Categoría', 'Precio'))
        self.tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)  
        self.tree.heading('#0', text='ID')
        self.tree.heading('Producto', text='Producto')
        self.tree.heading('Categoría', text='Categoría')
        self.tree.heading('Precio', text='Precio')
        self.tree.bind('<ButtonRelease-1>', self.select_product)

        self.show_products()
        
        return self.frame
