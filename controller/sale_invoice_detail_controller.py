from model.sale_invoice_detail import SaleInvoiceDetail

class SaleInvoiceDetailController:
    def __init__(self):
        self.sale_invoice_detail = SaleInvoiceDetail()

    def create_invoice_detail(self, invoice_id, product_id, quantity, unit_price, total_income):
        self.sale_invoice_detail.create_invoice_detail(invoice_id, product_id, quantity, unit_price, total_income)

    def delete_invoice_detail(self, detail_id):
        self.sale_invoice_detail.delete_invoice_detail(detail_id)
