import psycopg2
from database.database import Database

class Summary:
    def __init__(self):
        self.db = Database()

    def get_total_sales(self):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            cursor.execute("SELECT COALESCE(SUM(ingreso_total), 0) FROM Detalle_F_Venta")
            total_sales = cursor.fetchone()[0]
            self.db.close_connection()
            return total_sales
        except psycopg2.Error as ex:
            print('Error al obtener las ventas totales: ', ex)

    def get_total_purchases(self):
        try:
            self.db.connect()
            cursor = self.db.get_cursor()
            cursor.execute("SELECT COALESCE(SUM(gasto_total), 0) FROM Detalle_F_Compra")
            total_purchases = cursor.fetchone()[0]
            self.db.close_connection()
            return total_purchases
        except psycopg2.Error as ex:
            print('Error al obtener las compras totales: ', ex)
    