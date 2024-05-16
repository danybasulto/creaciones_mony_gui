import psycopg2
from database.database import Database

class PurchaseInvoiceDetail:
    def __init__(self):
        self.db = Database()

    def create_invoice_detail(self, invoice_id, product_id, quantity):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            # Obtener el precio unitario del producto desde la base de datos
            cursor.execute("SELECT precio FROM Producto WHERE id_producto = %s", (product_id,))
            unit_price = cursor.fetchone()[0]
            total_expense = quantity * unit_price
            # Insertar el detalle de la factura de compra con el precio unitario y el gasto total
            query = """INSERT INTO Detalle_F_Compra (folio_compra, producto, cantidad, precio_compra, gasto_total) 
                       VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (invoice_id, product_id, quantity, unit_price, total_expense))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nDetalle de factura de compra creado exitosamente.')
            return unit_price, total_expense  # Devolver el precio unitario y el gasto total
        except psycopg2.Error as ex:
            print('Error al crear el detalle de factura de compra: ', ex)
            return None, None

    def get_purchase_invoices(self):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            cursor.execute("SELECT folio_compra FROM Factura_Compra")
            invoices = cursor.fetchall()
            self.db.close_connection()
            return invoices if invoices else []
        except psycopg2.Error as ex:
            print('Error al obtener las facturas de compra: ', ex)
            return []

    def get_products(self):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            cursor.execute("SELECT id_producto, nombre FROM Producto")
            products = cursor.fetchall()
            self.db.close_connection()
            return products if products else []
        except psycopg2.Error as ex:
            print('Error al obtener los productos: ', ex)
            return []

    def get_product_details(self, product_id):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            cursor.execute("SELECT nombre, precio FROM Producto WHERE id_producto = %s", (product_id,))
            product_details = cursor.fetchone()
            self.db.close_connection()
            return product_details if product_details else []
        except psycopg2.Error as ex:
            print('Error al obtener los detalles del producto: ', ex)
            return []
