from model.provider import Provider

class ProviderController:
    def __init__(self):
        self.provider = Provider()

    def create(self, bn, cn, a, pn):
        self.provider.create(bn, cn, a, pn)
        
    def read(self):
        return self.provider.read()

    def update(self, id, b_name, c_name, address, phone_number):
        self.provider.update(id, b_name, c_name, address, phone_number)

    def delete(self, id):
        self.provider.delete(id)

    def find(self, b_name):
        self.provider.find(b_name)
