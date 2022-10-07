import sqlite3


class Finance:
    def __init__(self, file_path):
        try:
            self.conn = sqlite3.connect(file_path)
            self.c = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)

    def create_new_table(self, year: int):
        """
        Create new table with name of the year
        :param year: The part of table name. The example of the full name: YEAR_2022
        """
        query = f"""CREATE TABLE IF NOT EXISTS YEAR_{year} (
                          Month text,
                          Income text,
                          VAT costs text,
                          Tax costs text,
                          ZUS costs text,
                          Payout text
                          )"""
        self.c.execute(query)
        self.conn.commit()

    def add_value_to_table(self, year: int, data: dict):
        """
        Add values to the table.
        :param year: The table name
        :param data: It should contain the following data: month, income, vat, tax, zus, payout
        """
        query = f"INSERT INTO YEAR_{year} VALUES (:month, :income, :vat, :tax, :zus, :payout)"
        self.c.execute(query, {"month": data['month'], "income": data['income'], "vat": data['vat'], "tax": data['tax'],
                               "zus": data['zus'], "payout": data['payout']})
        self.conn.commit()

    def read_values_from_month(self, year: int, month: str) -> tuple:
        """
        Read all values from the specific month.
        :param year: The table name
        :param month: Specific month what should be read
        :return: All information from the month in tuple: month, income, vat, tax, zus, payout
        """
        query = f"SELECT * FROM YEAR_{year} WHERE month='{month}'"
        self.c.execute(query)

        return self.c.fetchone()

    def update_value_in_month(self, year: int, column, old_value, new_value):
        """
        Update value in the specific month.
        :param year: The table name
        :param column: The name of the column to be changed
        :param old_value: Value to change
        :param new_value: New value
        """
        query = f"UPDATE YEAR_{year} SET {column} = \"{new_value}\" WHERE {column} = \"{old_value}\""
        self.c.execute(query)
        self.conn.commit()


finance = Finance('finance.db')

all_data = {"month": "February", "income": 16500, "vat": 3605, "tax": 2500, "zus": 1500, "payout": 9500}

table_name = 2022
# finance.create_new_table(table_name)
# finance.add_value_to_table(table_name, all_data)
# finance.read_values_from_month(table_name, "February")
finance.update_value_in_month(table_name, 'month', 'January', 'March')
