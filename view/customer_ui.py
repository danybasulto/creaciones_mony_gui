import tkinter as tk
from tkinter import StringVar, ttk, Entry, Label
from controller.customer_controller import CustomerController

class CustomerUI:
    def __init__(self, root, regresar_menu):
        self.root = root
        self.regresar_menu = regresar_menu
        self.customer_controller = CustomerController()

    def regresar_menu(self):
        self.root.menu()

    def clear_fields(self):
        self.id_var.set('')
        self.first_name_var.set('')
        self.last_name_var.set('')
        self.address_var.set('')
        self.phone_number_var.set('')

    def show_customers(self):
        self.clear_fields()
        customers = self.customer_controller.read()
        self.tree.delete(*self.tree.get_children())
        for customer in customers:
            self.tree.insert('', 'end', text=customer[0], values=(customer[1], customer[2], customer[3], customer[4]))

    def select_customer(self, event):
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, 'values')
        self.id_var.set(self.tree.item(selected_item, 'text'))
        self.first_name_var.set(values[0])
        self.last_name_var.set(values[1])
        self.address_var.set(values[2])
        self.phone_number_var.set(values[3])

    def create_customer(self):
        first_name = self.first_name_var.get()
        last_name = self.last_name_var.get()
        address = self.address_var.get()
        phone_number = self.phone_number_var.get()
        self.customer_controller.create(first_name, last_name, address, phone_number)
        self.show_customers()

    def update_customer(self):
        customer_id = self.id_var.get()
        first_name = self.first_name_var.get()
        last_name = self.last_name_var.get()
        address = self.address_var.get()
        phone_number = self.phone_number_var.get()
        self.customer_controller.update(customer_id, first_name, last_name, address, phone_number)
        self.show_customers()

    def delete_customer(self):
        customer_id = self.id_var.get()
        self.customer_controller.delete(customer_id)
        self.show_customers()

    def find_customer(self):
        first_name = self.first_name_var.get()
        customers = self.customer_controller.find(first_name)
        if customers:
            self.tree.delete(*self.tree.get_children())
            for customer in customers:
                self.tree.insert('', 'end', text=customer[0], values=(customer[1], customer[2], customer[3], customer[4]))
        else:
            print('No se encontraron clientes con ese nombre.')

    def start_gui(self):
        self.id_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.address_var = StringVar()
        self.phone_number_var = StringVar()

        frame = ttk.Frame(self.root)
        frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Botón de regreso al menú principal
        boton_regresar = ttk.Button(frame, text="Menú Principal", command=self.regresar_menu)
        boton_regresar.pack(side=tk.LEFT, padx=5, pady=5)

        Label(frame, text='ID:').pack()  
        Entry(frame, textvariable=self.id_var, state='readonly').pack()  

        Label(frame, text='Nombre(s):').pack()  
        Entry(frame, textvariable=self.first_name_var).pack()  

        Label(frame, text='Apellido(s):').pack()  
        Entry(frame, textvariable=self.last_name_var).pack()  

        Label(frame, text='Dirección:').pack()  
        Entry(frame, textvariable=self.address_var).pack()  

        Label(frame, text='Número de Teléfono:').pack()  
        Entry(frame, textvariable=self.phone_number_var).pack()  

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack()  

        ttk.Button(btn_frame, text='Agregar Cliente', command=self.create_customer).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(btn_frame, text='Modificar Cliente', command=self.update_customer).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(btn_frame, text='Eliminar Cliente', command=self.delete_customer).pack(side=tk.LEFT, padx=5, pady=5)  
        ttk.Button(btn_frame, text='Buscar Cliente', command=self.find_customer).pack(side=tk.LEFT, padx=5, pady=5)  

        self.tree = ttk.Treeview(self.root, columns=('Nombre(s)', 'Apellido(s)', 'Dirección', 'Número de Teléfono'))
        self.tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)  
        self.tree.heading('#0', text='ID')
        self.tree.heading('Nombre(s)', text='Nombre(s)')
        self.tree.heading('Apellido(s)', text='Apellido(s)')
        self.tree.heading('Dirección', text='Dirección')
        self.tree.heading('Número de Teléfono', text='Número de Teléfono')
        self.tree.bind('<ButtonRelease-1>', self.select_customer)

        return frame
