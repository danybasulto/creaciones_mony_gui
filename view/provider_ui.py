import tkinter as tk
from tkinter import ttk, Entry, Label
from controller.provider_controller import ProviderController

class ProviderUI:
    def __init__(self, root):
        self.root = root
        self.provider_controller = ProviderController()
        self.frame = None
        
        # Inicializar variables de cadena
        self.id_var = tk.StringVar()
        self.bussiness_name_var = tk.StringVar()
        self.contact_name_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.phone_number_var = tk.StringVar()

    def go_back_to_menu(self):
        self.hide()
        self.root.menu()

    def clear_fields(self):
        self.id_var.set('')
        self.bussiness_name_var.set('')
        self.contact_name_var.set('')
        self.address_var.set('')
        self.phone_number_var.set('')

    def show_providers(self):
        self.clear_fields()
        self.tree.delete(*self.tree.get_children())
        for provider in self.provider_controller.read():
            self.tree.insert('', 'end', text=provider[0], values=(provider[1], provider[2], provider[3], provider[4]))

    def select_provider(self, event):
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, 'values')
        self.id_var.set(self.tree.item(selected_item, 'text'))
        self.bussiness_name_var.set(values[0])
        self.contact_name_var.set(values[1])
        self.address_var.set(values[2])
        self.phone_number_var.set(values[3])

    def create_provider(self):
        bussiness_name = self.bussiness_name_var.get()
        contact_name = self.contact_name_var.get()
        address = self.address_var.get()
        phone_number = self.phone_number_var.get()
        self.provider_controller.create(bussiness_name, contact_name, address, phone_number)
        self.show_providers()

    def update_provider(self):
        provider_id = self.id_var.get()
        bussiness_name = self.bussiness_name_var.get()
        contact_name = self.contact_name_var.get()
        address = self.address_var.get()
        phone_number = self.phone_number_var.get()
        self.provider_controller.update(provider_id, bussiness_name, contact_name, address, phone_number)
        self.show_providers()

    def delete_provider(self):
        provider_id = self.id_var.get()
        self.provider_controller.delete(provider_id)
        self.show_providers()

    def find_provider(self):
        bussiness_name = self.bussiness_name_var.get()
        providers = self.provider_controller.find(bussiness_name)
        if providers:
            self.tree.delete(*self.tree.get_children())
            for provider in providers:
                self.tree.insert('', 'end', text=provider[0], values=(provider[1], provider[2], provider[3], provider[4]))
        else:
            print('No se encontraron proveedores con ese nombre.')

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

        Label(self.frame, text='Nombre del negocio:').pack()  
        Entry(self.frame, textvariable=self.bussiness_name_var).pack()  

        Label(self.frame, text='Nombre del contacto:').pack()  
        Entry(self.frame, textvariable=self.contact_name_var).pack()  

        Label(self.frame, text='Dirección:').pack()  
        Entry(self.frame, textvariable=self.address_var).pack()  

        Label(self.frame, text='Número de Teléfono:').pack()  
        Entry(self.frame, textvariable=self.phone_number_var).pack()  

        button_frame = ttk.Frame(self.frame)  # Crear un marco para los botones
        button_frame.pack()  

        ttk.Button(button_frame, text='Agregar Proveedor', command=self.create_provider).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(button_frame, text='Modificar Proveedor', command=self.update_provider).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(button_frame, text='Eliminar Proveedor', command=self.delete_provider).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(button_frame, text='Buscar Proveedor', command=self.find_provider).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(button_frame, text='Limpiar campos', command=self.clear_fields).pack(side=tk.LEFT, padx=5, pady=5)

        # Crear la tabla dentro del marco principal
        self.tree = ttk.Treeview(self.frame, columns=('Nombre del negocio', 'Nombre del contacto', 'Dirección', 'Número de Teléfono'))
        self.tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)  
        self.tree.heading('#0', text='ID')
        self.tree.heading('Nombre del negocio', text='Nombre del negocio')
        self.tree.heading('Nombre del contacto', text='Nombre del contacto')
        self.tree.heading('Dirección', text='Dirección')
        self.tree.heading('Número de Teléfono', text='Número de Teléfono')
        self.tree.bind('<ButtonRelease-1>', self.select_provider)

        # Llamar a show_providers para mostrar los proveedores en la tabla
        self.show_providers()

        return self.frame
