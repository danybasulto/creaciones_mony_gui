from model.purchase_invoice import PurchaseInvoice

class PurchaseInvoiceController:
    def __init__(self):
        self.purchase_invoice = PurchaseInvoice()

    def create_invoice(self, supplier_id, date):
        self.purchase_invoice.create_invoice(supplier_id, date)

    def read_invoices(self):
        self.purchase_invoice.read_invoices()

    def update_invoice(self, invoice_id, supplier_id, date):
        self.purchase_invoice.update_invoice(invoice_id, supplier_id, date)

    def delete_invoice(self, invoice_id):
        self.purchase_invoice.delete_invoice(invoice_id)
