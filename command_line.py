from finance import Finance
import sys
import os


class CommandLine(Finance):
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
        year = int(input("Enter the year: "))
        data = self._prepare_data_for_one_month()
        self.add_value_to_table(year, data)
        self._clear_console()
        self.main_thread()

    def response_read_values(self):
        """
        Read all values from the selected month
        """
        year = int(input("Enter the year: "))
        month = input("Enter the month: ")  # TODO: add security in the event that there is no such month
        month, income, vat, tax, zus, payout = self.read_values_from_month(year, month)
        input(f"Month: {month}, Income: {income}, VAT: {vat}, Tax: {tax}, ZUS: {zus}, Payout: {payout}")
        self._clear_console()
        self.main_thread()

    def response_update_values(self):
        """
        Updating the value in the selected column
        """
        year = int(input("Enter the year: "))
        column = input("Enter the column you want to make changes to: ")  # TODO: add security in the event that there is no such column
        old_value = input("Enter the old value: ")  # TODO: add security in the event that there is no such value
        new_value = input("Enter the new value: ")
        self.update_value_in_month(year, column, old_value, new_value)
        self._clear_console()
        self.main_thread()

    def response_delete_month(self):
        """
        Removing the month from the selected table
        """
        year = int(input("Enter the year: "))
        month = input("Enter the month: ")  # TODO: add security in the event that there is no such month
        self.delete_month(year, month)
        self._clear_console()
        self.main_thread()

    def response_visualize(self):
        """
        Visualization of finance statistics
        """
        input("Coming soon!")
        self._clear_console()
        self.main_thread()

    @staticmethod
    def response_exit():
        """
        Safely quitting the program
        """
        sys.exit()
        # TODO: add closing finance.db file

    @staticmethod
    def _show_main_view():
        """
        Show main view for the user and get a response from him
        :return: Response with chosen number
        """
        # TODO: add security in the event that there is wrong response from the user
        return input("What do you want to do?\n\n"
                     "1. Create new table\n"
                     "2. Add new month to the table\n"
                     "3. Read values from specific month\n"
                     "4. Update values in specific month\n"
                     "5. Delete month from table\n"
                     "6. Visualize finance statistics\n"
                     "7. Exit\n\n"
                     "Your choice: ")

    def _prepare_data_for_one_month(self):
        """
        Prepare all needed information for one month in specific dict format
        :return:
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
