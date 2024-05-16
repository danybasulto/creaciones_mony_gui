from model.sale_invoice import SaleInvoice

from controller.customer_controller import CustomerController

class SaleInvoiceController:
    def __init__(self):
        self.sale_invoice = SaleInvoice()
        self.customer_controller = CustomerController()

    def create_invoice(self, client_id, date):
        self.sale_invoice.create_invoice(client_id, date)

    def read_invoices(self):
        return self.sale_invoice.read_invoices()

    def update_invoice(self, invoice_id, client_id, date):
        self.sale_invoice.update_invoice(invoice_id, client_id, date)

    def delete_invoice(self, invoice_id):
        self.sale_invoice.delete_invoice(invoice_id)

    def get_customers(self):
        return self.customer_controller.read()
    
    def get_customer_name(self, customer_id):
        return self.customer_controller.get_customer_name(customer_id)
