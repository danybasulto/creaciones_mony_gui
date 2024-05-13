import psycopg2
from database.database import Database

class SaleInvoice:
    def __init__(self):
        self.db = Database()

    def create_invoice(self, client_id, date):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            query = """INSERT INTO Factura_Venta (cliente, fecha) VALUES (%s, %s)"""
            cursor.execute(query, (client_id, date))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nFactura de Venta creada exitosamente.')
        except psycopg2.Error as ex:
            print('Error al crear la Factura de Venta: ', ex)

    def read_invoices(self):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            cursor.execute("SELECT * FROM Factura_Venta")
            rows = cursor.fetchall()
            self.db.close_connection()

            if len(rows) == 0:
                print('No hay Facturas de Venta.')
            else:
                print('Facturas de Venta:')
                for row in rows:
                    print(row)
        except psycopg2.Error as ex:
            print('Error al mostrar las Facturas de Venta: ', ex)

    def update_invoice(self, invoice_id, client_id, date):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            query = """UPDATE Factura_Venta SET cliente=%s, fecha=%s WHERE folio_venta=%s"""
            cursor.execute(query, (client_id, date, invoice_id))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nFactura de Venta actualizada exitosamente.')
        except psycopg2.Error as ex:
            print('Error al actualizar la Factura de Venta: ', ex)

    def delete_invoice(self, invoice_id):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            query = """DELETE FROM Factura_Venta WHERE folio_venta=%s"""
            cursor.execute(query, (invoice_id,))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nFactura de Venta eliminada exitosamente.')
        except psycopg2.Error as ex:
            print('Error al eliminar la Factura de Venta: ', ex)
