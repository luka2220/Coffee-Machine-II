import sqlite3


class CoffeeDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('coffee_machine_database.db')

    def save_data(self, date, item, amount):
        self.connection.execute(f"INSERT INTO SALES VALUES('{date}', '{item}', '{amount}')")
        self.connection.commit()

    def get_data(self):
        data = self.connection.execute("SELECT * FROM SALES")
        return data

    def close_connection(self):
        self.connection.close()
