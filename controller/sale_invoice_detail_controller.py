from model.sale_invoice_detail import SalesInvoiceDetail

class SalesInvoiceDetailController:
    def __init__(self):
        self.sales_invoice_detail = SalesInvoiceDetail()

    def create_invoice_detail(self, invoice_id, product_id, quantity):
        return self.sales_invoice_detail.create_invoice_detail(invoice_id, product_id, quantity)

    def get_sales_invoices(self):
        return self.sales_invoice_detail.get_sales_invoices()

    def get_products(self):
        return self.sales_invoice_detail.get_products()

    def get_product_details(self, product_id):
        return self.sales_invoice_detail.get_product_details(product_id)
