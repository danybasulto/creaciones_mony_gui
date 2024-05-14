import tkinter as tk
from tkinter import ttk, Entry, Label, messagebox
from controller.category_controller import CategoryController

class CategoryUI:
    def __init__(self, root):
        self.root = root
        self.category_controller = CategoryController()
        self.frame = None
        
        # Inicializar variables de cadena
        self.id_var = tk.StringVar()
        self.name_var = tk.StringVar()

    def go_back_to_menu(self):
        self.hide()
        self.root.menu()

    def clear_fields(self):
        self.id_var.set('')
        self.name_var.set('')

    def select_category(self, event):
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, 'values')
        self.id_var.set(self.tree.item(selected_item, 'text'))
        self.name_var.set(values[0])

    def create_category(self):
        name = self.name_var.get()
        self.category_controller.create(name)
        messagebox.showinfo("Información", "Categoría creada exitosamente.")
        self.clear_fields()

    def read_categories(self):
        categories = self.category_controller.read()
        if categories:
            for category in categories:
                self.tree.insert('', 'end', text=category[0], values=(category[1],))
        else:
            print("No hay categorías registradas.")

    def update_category(self):
        id = self.id_var.get()
        name = self.name_var.get()
        self.category_controller.update(id, name)
        messagebox.showinfo("Información", "Categoría actualizada exitosamente.")
        self.clear_fields()

    def delete_category(self):
        id = self.id_var.get()
        self.category_controller.delete(id)
        messagebox.showinfo("Información", "Categoría eliminada exitosamente.")
        self.clear_fields()

    def find_category(self):
        name = self.name_var.get()
        categories = self.category_controller.find(name)
        if categories:
            messagebox.showinfo("Categoría encontrada", "\n".join(categories))
        else:
            messagebox.showinfo("Información", "No se encontraron categorías con ese nombre.")

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

        Label(self.frame, text='ID:').pack()  
        Entry(self.frame, textvariable=self.id_var, state='readonly').pack()  

        Label(self.frame, text='Nombre:').pack()  
        Entry(self.frame, textvariable=self.name_var).pack()  

        button_frame = ttk.Frame(self.frame)  # Crear un marco para los botones
        button_frame.pack()  

        ttk.Button(button_frame, text='Agregar Categoría', command=self.create_category).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(button_frame, text='Modificar Categoría', command=self.update_category).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(button_frame, text='Eliminar Categoría', command=self.delete_category).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(button_frame, text='Buscar Categoría', command=self.find_category).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(button_frame, text='Limpiar campos', command=self.clear_fields).pack(side=tk.LEFT, padx=5, pady=5)

        # Crear la tabla dentro del marco principal
        self.tree = ttk.Treeview(self.frame, columns=('Nombre',))
        self.tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)  
        self.tree.heading('#0', text='ID')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.bind('<ButtonRelease-1>', self.select_category)

        # Llamar a read_categories para mostrar las categorías en la tabla
        self.read_categories()

        return self.frame
