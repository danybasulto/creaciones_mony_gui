from tkinter import Tk, StringVar, ttk, Menu, Entry, Label, Button
from controller.customer_controller import CustomerController

class CustomerUI:
    def __init__(self):
        self.customer_controller = CustomerController()

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
        root = Tk()
        root.title('Gestión de Clientes')

        self.id_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.address_var = StringVar()
        self.phone_number_var = StringVar()

        frame = ttk.Frame(root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        Label(frame, text='ID:').grid(row=0, column=0, padx=5, pady=5)
        Entry(frame, textvariable=self.id_var, state='readonly').grid(row=0, column=1, padx=5, pady=5)

        Label(frame, text='Nombre(s):').grid(row=1, column=0, padx=5, pady=5)
        Entry(frame, textvariable=self.first_name_var).grid(row=1, column=1, padx=5, pady=5)

        Label(frame, text='Apellido(s):').grid(row=2, column=0, padx=5, pady=5)
        Entry(frame, textvariable=self.last_name_var).grid(row=2, column=1, padx=5, pady=5)

        Label(frame, text='Dirección:').grid(row=3, column=0, padx=5, pady=5)
        Entry(frame, textvariable=self.address_var).grid(row=3, column=1, padx=5, pady=5)

        Label(frame, text='Número de Teléfono:').grid(row=4, column=0, padx=5, pady=5)
        Entry(frame, textvariable=self.phone_number_var).grid(row=4, column=1, padx=5, pady=5)

        btn_frame = ttk.Frame(root)
        btn_frame.grid(row=1, column=0, padx=10, pady=10)

        ttk.Button(btn_frame, text='Agregar Cliente', command=self.create_customer).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text='Modificar Cliente', command=self.update_customer).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text='Eliminar Cliente', command=self.delete_customer).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(btn_frame, text='Buscar Cliente', command=self.find_customer).grid(row=0, column=3, padx=5, pady=5)

        self.tree = ttk.Treeview(root, columns=('Nombre(s)', 'Apellido(s)', 'Dirección', 'Número de Teléfono'))
        self.tree.grid(row=2, column=0, padx=10, pady=10)
        self.tree.heading('#0', text='ID')
        self.tree.heading('Nombre(s)', text='Nombre(s)')
        self.tree.heading('Apellido(s)', text='Apellido(s)')
        self.tree.heading('Dirección', text='Dirección')
        self.tree.heading('Número de Teléfono', text='Número de Teléfono')
        self.tree.bind('<ButtonRelease-1>', self.select_customer)

        root.mainloop()
