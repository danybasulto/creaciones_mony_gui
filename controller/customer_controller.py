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
