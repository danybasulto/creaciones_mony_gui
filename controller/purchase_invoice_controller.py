from model.purchase_invoice import PurchaseInvoice
from controller.provider_controller import ProviderController

class PurchaseInvoiceController:
    def __init__(self):
        self.purchase_invoice = PurchaseInvoice()
        self.provider_controller = ProviderController()

    def create_invoice(self, supplier_id, date):
        self.purchase_invoice.create_invoice(supplier_id, date)
        
    def read_invoices(self):
        return self.purchase_invoice.read_invoices()

    def update_invoice(self, invoice_id, supplier_id, date):
        self.purchase_invoice.update_invoice(invoice_id, supplier_id, date)

    def delete_invoice(self, invoice_id):
        self.purchase_invoice.delete_invoice(invoice_id)

    def get_suppliers(self):
        return self.provider_controller.read()
    
    def get_supplier_name(self, supplier_id):
        return self.provider_controller.get_supplier_name(supplier_id)