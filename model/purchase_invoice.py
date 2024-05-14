import psycopg2
from database.database import Database

class PurchaseInvoice:
    def __init__(self):
        self.db = Database()

    def create_invoice(self, supplier_id, date):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            query = """INSERT INTO Factura_Compra (proveedor, fecha) VALUES (%s, %s)"""
            cursor.execute(query, (supplier_id, date))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nFactura de Compra creada exitosamente.')
        except psycopg2.Error as ex:
            print('Error al crear la Factura de Compra: ', ex)

    def read_invoices(self):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            cursor.execute("SELECT * FROM Factura_Compra")
            rows = cursor.fetchall()
            self.db.close_connection()
            if len(rows) == 0:
                return []
            else:
                return rows
        except psycopg2.Error as ex:
            print('Error al mostrar las Facturas de Compra: ', ex)
            return []

    def update_invoice(self, invoice_id, supplier_id, date):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            query = """UPDATE Factura_Compra SET proveedor=%s, fecha=%s WHERE folio_compra=%s"""
            cursor.execute(query, (supplier_id, date, invoice_id))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nFactura de Compra actualizada exitosamente.')
        except psycopg2.Error as ex:
            print('Error al actualizar la Factura de Compra: ', ex)

    def delete_invoice(self, invoice_id):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            query = """DELETE FROM Factura_Compra WHERE folio_compra=%s"""
            cursor.execute(query, (invoice_id,))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nFactura de Compra eliminada exitosamente.')
        except psycopg2.Error as ex:
            print('Error al eliminar la Factura de Compra: ', ex)
