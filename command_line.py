from data_visualization import DataVisualization
import sys
import os


class CommandLine(DataVisualization):
    needed_data_for_month = ["month", "income", "vat", "tax", "zus"]

    def __init__(self):
        print("Welcome in Finance Statistics application!")
        self.response_options = {"1": self.response_create_new_table,
                                 "2": self.response_add_new_month,
                                 "3": self.response_read_values,
                                 "4": self.response_update_values,
                                 "5": self.response_delete_month,
                                 "6": self.response_visualize,
                                 "7": self.response_exit}
        super().__init__()

    def main_thread(self):
        """
        Main thread serving the user's console
        """
        response = self._show_main_view()
        self.response_options[response]()

    def response_create_new_table(self):
        """
        Create new table
        """
        year = int(input("Enter the year: "))
        self.create_new_table(year)
        self._clear_console()
        self.main_thread()

    def response_add_new_month(self):
        """
        Add new month to the selected year
        """
        # TODO: add security on the event when year is wrong
        year = int(input("Enter the year: "))
        data = self._prepare_data_for_one_month()
        self.add_value_to_table(year, data)
        self._clear_console()
        self.main_thread()

    def response_read_values(self):
        """
        Read all values from the selected month
        """
        month_flag = False
        year = int(input("Enter the year: "))

        while month_flag is False:
            month = input("Enter the month: ")
            month_flag = self._verify_value_in_the_column(year, "month", month)

        month, income, vat, tax, zus, payout = self.get_values_from_month(year, month)
        input(f"Month: {month}, Income: {income}, VAT: {vat}, Tax: {tax}, ZUS: {zus}, Payout: {payout}")
        self._clear_console()
        self.main_thread()

    def response_update_values(self):
        """
        Updating the value in the selected column
        """

        column_flag, value_flag = False, False
        year = int(input("Enter the year: "))

        while column_flag is False:
            column = input("Enter the column you want to make changes to: ")
            column_flag = self._verify_column_name(year, column)

        while value_flag is False:
            old_value = input("Enter the old value: ")
            value_flag = self._verify_value_in_the_column(year, column, old_value)

        new_value = input("Enter the new value: ")
        self.update_value_in_month(year, column, old_value, new_value)
        self._clear_console()
        self.main_thread()

    def response_delete_month(self):
        """
        Removing the month from the selected table
        """
        month_flag = False
        year = int(input("Enter the year: "))

        while month_flag is False:
            month = input("Enter the month: ")
            month_flag = self._verify_value_in_the_column(year, "month", month)

        self.delete_month(year, month)
        self._clear_console()
        self.main_thread()

    def response_visualize(self):
        """
        Visualization of finance statistics
        """
        year = input("Enter the year: ")
        self.year_plot(year)
        self.years_comparison()
        self._clear_console()
        self.main_thread()

    def response_exit(self):
        """
        Safely quitting the program
        """
        self.conn.close()
        sys.exit()

    def _show_main_view(self):
        """
        Show main view for the user and get a response from him
        :return: Response with chosen number
        """
        response_flag = False
        while response_flag is False:
            response = input("What do you want to do?\n\n"
                             "1. Create new table\n"
                             "2. Add new month to the table\n"
                             "3. Read values from specific month\n"
                             "4. Update values in specific month\n"
                             "5. Delete month from table\n"
                             "6. Visualize finance statistics\n"
                             "7. Exit\n\n"
                             "Your choice: ")
            response_flag = self._verify_chosen_number(response)
        return response

    def _verify_chosen_number(self, response):
        """
        Verification chosen number in main view. When is not correct, the function return False
        :param response: User response from main view
        :return: False when the response is wrong
        """
        if response not in self.response_options.keys():
            input("You choose wrong number! Try again.")
            return False

    def _verify_value_in_the_column(self, year, column, value):
        """
        Verification whether the given value appears in a given column
        :param year: The table name
        :param column: The column name
        :param value: Value in specified column
        :return: False when the value is wrong
        """
        values = self.get_values_from_column(year, column)
        if value not in values:
            input(f"You choose wrong value!\n"
                  f"Correct values: {values}")
            return False

    def _verify_column_name(self, year, column):
        """
        Verification if the given column name exists
        :param year: The table name
        :param column: The column name
        :return: False if column name is wrong
        """
        columns = self.get_column_names(year)
        if column not in columns:
            input(f"You choose wrong column name!\n"
                  f"Correct values: {columns}")
            return False

    def _prepare_data_for_one_month(self):
        """
        Prepare all needed information for one month in specific dict format
        :return: Data in an appropriately prepared dictionary format
        """
        data = self._get_information_from_user()
        data = self._change_format_to_float(data)
        data = self._calculate_payout(data)
        return data

    def _get_information_from_user(self) -> dict:
        """
        Use console input for get the information from the user
        :return: Introductory dictionary with user data
        """
        data = {}
        print("Enter the required data:")
        for information in self.needed_data_for_month:
            user_input = input(information + ": ")
            data[information] = user_input

        return data

    @staticmethod
    def _change_format_to_float(data: dict) -> dict:
        """
        Change all data format to float without month value
        :param data: Prepared dictionary from _get_information_from_user() function
        :return: The same dictionary with corrected data format
        """
        for key, value in data.items():
            if key == 'month':
                continue
            data[key] = float(value)

        return data

    @staticmethod
    def _calculate_payout(data: dict) -> dict:
        """
        Payout calculation based on user values
        :param data: Prepared dictionary with float data format
        :return: Dictionary with added payout
        """
        payout = data['income'] - data['vat'] - data['tax'] - data['zus']
        data['payout'] = payout

        return data

    @staticmethod
    def _clear_console():
        """
        Clear user console after making selection
        """
        os.system('cls')


cmd = CommandLine()
cmd.main_thread()
