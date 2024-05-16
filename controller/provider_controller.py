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
        
    def get_supplier_name(self, supplier_id):
            supplier = self.provider.read()  # Cambio aquí, se obtienen todos los proveedores
            for row in supplier:
                if row[0] == supplier_id:  # Suponiendo que el ID del proveedor está en la primera posición de la tupla
                    return row[1]  # Suponiendo que el nombre del proveedor está en la segunda posición de la tupla
            return "Proveedor Desconocido"