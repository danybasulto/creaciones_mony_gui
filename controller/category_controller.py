from model.category import Category

class CategoryController:
    def __init__(self):
        self.category = Category()

    def create(self, name):
        self.category.create(name)
        
    def read(self):
        return self.category.read()

    def update(self, id, name):
        self.category.update(id, name)

    def delete(self, id):
        self.category.delete(id)

    def find(self, name):
        self.category.find(name)
