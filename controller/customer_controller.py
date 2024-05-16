from model.customer import Customer

class CustomerController:
    def __init__(self):
        self.customer = Customer()

    def create(self, fn, ln, a, pn):
        self.customer.create(fn, ln, a, pn)
        
    def read(self):
        customers = self.customer.read()
        if customers is None:
            customers = []
        return customers

    def update(self, id, first_name, last_name, address, phone_number):
        self.customer.update(id, first_name, last_name, address, phone_number)

    def delete(self, id):
        self.customer.delete(id)

    def find(self, first_name):
        return self.customer.find(first_name)
    
    def get_customer_name(self, customer_id):
        customers = self.customer.read()
        for customer in customers:
            if customer[0] == customer_id:  # Suponiendo que el ID del cliente está en la primera posición de la tupla
                return f"{customer[1]} {customer[2]}"  # Suponiendo que el primer nombre está en la segunda posición y el apellido en la tercera posición de la tupla
        return "Cliente Desconocido"