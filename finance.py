import sqlite3


class Finance:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('finance.db')
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

    def read_values_from_column(self, year: int, column: str) -> list:
        """
        Return all values from selected column
        :param year: The table name
        :param column: The column name
        :return: List of values in selected column
        """
        query = f"SELECT {column} FROM YEAR_{year}"
        self.c.execute(query)
        return [value[0] for value in self.c.fetchall()]

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

    def delete_month(self, year: int, month: str):
        """
        Delete whole month from the table.
        :param year: The table name
        :param month: The name of the month to be deleted
        """
        query = f"DELETE FROM YEAR_{year} WHERE month=\"{month}\""
        self.c.execute(query)
        self.conn.commit()

    def get_column_names(self, year: int) -> list:
        """
        Return a complete list of column names
        :param year: The table name
        :return: List of column names
        """
        cursor = self.c.execute(f"SELECT * FROM YEAR_{year}")
        return list(map(lambda value: value[0].lower(), cursor.description))
