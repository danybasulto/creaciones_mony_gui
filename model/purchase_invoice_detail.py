import psycopg2
from database.database import Database

class PurchaseInvoiceDetail:
    def __init__(self):
        self.db = Database()

    def create_invoice_detail(self, invoice_id, product_id, quantity, unit_price, total_expense):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            query = """INSERT INTO Detalle_F_Compra (folio_compra, producto, cantidad, precio_compra, gasto_total)
                       VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (invoice_id, product_id, quantity, unit_price, total_expense))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nDetalle de Factura de Compra creado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al crear el Detalle de Factura de Compra: ', ex)

    def delete_invoice_detail(self, detail_id):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            query = """DELETE FROM Detalle_F_Compra WHERE id_detalle=%s"""
            cursor.execute(query, (detail_id,))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nDetalle de Factura de Compra eliminado exitosamente.')
        except psycopg2.Error as ex:
            print('Error al eliminar el Detalle de Factura de Compra: ', ex)
