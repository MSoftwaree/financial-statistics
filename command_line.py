from finance import Finance
import sys
import os


class CommandLine(Finance):
    needed_data_for_month = ["month", "income", "vat", "tax", "zus"]

    def __init__(self):
        print("Welcome in Finance Statistics application!")
        super().__init__()

    def main_thread(self):
        response = self._show_main_view()

        if response == "1":
            year = int(input("Enter the year: "))
            self.create_new_table(year)
            self._clear_console()
            self.main_thread()

        elif response == "2":
            year = int(input("Enter the year: "))
            data = self._prepare_data_for_one_month()
            self.add_value_to_table(year, data)
            self._clear_console()
            self.main_thread()

        elif response == "3":
            year = int(input("Enter the year: "))
            month = input("Enter the month: ")  # TODO: add security in the event that there is no such month
            month, income, vat, tax, zus, payout = self.read_values_from_month(year, month)
            input(f"Month: {month}, Income: {income}, VAT: {vat}, Tax: {tax}, ZUS: {zus}, Payout: {payout}")
            self._clear_console()
            self.main_thread()

        elif response == "4":
            year = int(input("Enter the year: "))
            column = input("Enter the column you want to make changes to: ") # TODO: add security in the event that there is no such column
            old_value = input("Enter the old value: ")  # TODO: add security in the event that there is no such value
            new_value = input("Enter the new value: ")
            self.update_value_in_month(year, column, old_value, new_value)
            self._clear_console()
            self.main_thread()

        elif response == "5":
            year = int(input("Enter the year: "))
            month = input("Enter the month: ")  # TODO: add security in the event that there is no such month
            self.delete_month(year, month)
            self._clear_console()
            self.main_thread()

        elif response == "6":
            input("Coming soon!")
            self._clear_console()
            self.main_thread()

        elif response == "7":
            sys.exit()

    @staticmethod
    def _show_main_view():
        """
        Show main view for the user and get a response from him
        :return: Response with chosen number
        """
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
        os.system('cls')


cmd = CommandLine()
cmd.main_thread()
