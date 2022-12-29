from prettytable import PrettyTable


class SalesData:
    def __init__(self, sales_data):
        self.sales_data = sales_data
        self.table = PrettyTable()
        self.table.field_names = ["Date", "Drink Item", "Amount(Dollars)"]

    def view_sales(self):
        for row in self.sales_data:
            self.table.add_row([row[0], row[1], f"${row[2]}"])

    def print_sales(self):
        self.view_sales()
        print(self.table)


