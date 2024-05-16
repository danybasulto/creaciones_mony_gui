import psycopg2
from database.database import Database

class SalesInvoiceDetail:
    def __init__(self):
        self.db = Database()

    def create_invoice_detail(self, invoice_id, product_id, quantity):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            # Obtener el precio unitario del producto desde la base de datos
            cursor.execute("SELECT precio FROM Producto WHERE id_producto = %s", (product_id,))
            unit_price = cursor.fetchone()[0]
            total_income = quantity * unit_price
            # Insertar el detalle de la factura de venta con el precio unitario y el ingreso total
            query = """INSERT INTO Detalle_F_Venta (folio_venta, producto, cantidad, precio_venta, ingreso_total) 
                       VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (invoice_id, product_id, quantity, unit_price, total_income))
            self.db.connection.commit()
            self.db.close_connection()
            print('\nDetalle de factura de venta creado exitosamente.')
            return unit_price, total_income  # Devolver el precio unitario y el ingreso total
        except psycopg2.Error as ex:
            print('Error al crear el detalle de factura de venta: ', ex)
            return None, None

    def get_sales_invoices(self):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            cursor.execute("SELECT folio_venta FROM Factura_Venta")
            invoices = cursor.fetchall()
            self.db.close_connection()
            return invoices if invoices else []
        except psycopg2.Error as ex:
            print('Error al obtener las facturas de venta: ', ex)
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
