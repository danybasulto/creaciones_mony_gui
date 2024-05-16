from database.database import Database
from model.summary import Summary

class SummaryController:
    def __init__(self):
        self.db = Database()
        self.summary = Summary()

    def get_summary_data(self):
        total_sales = self.summary.get_total_sales()
        total_purchases = self.summary.get_total_purchases()
        balance = total_sales - total_purchases
        return total_sales, total_purchases, balance