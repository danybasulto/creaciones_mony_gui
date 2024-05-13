from model.purchase_invoice_detail import PurchaseInvoiceDetail

class PurchaseInvoiceDetailController:
    def __init__(self):
        self.purchase_invoice_detail = PurchaseInvoiceDetail()

    def create_invoice_detail(self, invoice_id, product_id, quantity, unit_price, total_expense):
        self.purchase_invoice_detail.create_invoice_detail(invoice_id, product_id, quantity, unit_price, total_expense)

    def delete_invoice_detail(self, detail_id):
        self.purchase_invoice_detail.delete_invoice_detail(detail_id)
