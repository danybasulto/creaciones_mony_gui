from model.purchase_invoice_detail import PurchaseInvoiceDetail

class PurchaseInvoiceDetailController:
    def __init__(self):
        self.purchase_invoice_detail = PurchaseInvoiceDetail()

    def create_invoice_detail(self, invoice_id, product_id, quantity):
        return self.purchase_invoice_detail.create_invoice_detail(invoice_id, product_id, quantity)

    def get_purchase_invoices(self):
        return self.purchase_invoice_detail.get_purchase_invoices()

    def get_products(self):
        return self.purchase_invoice_detail.get_products()

    def get_product_details(self, product_id):
        return self.purchase_invoice_detail.get_product_details(product_id)
