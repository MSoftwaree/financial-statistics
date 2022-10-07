from finance import Finance


class CommandLine:
    needed_data_for_month = ["month", "income", "vat", "tax", "zus"]

    def prepare_data_for_one_month(self):
        """
        Prepare all needed information for one month in specific dict format
        :return:
        """
        data = self._get_information_from_user()
        data = self._change_format_to_int(data)
        data = self._calculate_payout(data)
        print(data)

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
    def _change_format_to_int(data: dict) -> dict:
        """
        Change all data format to integer without month value
        :param data: Prepared dictionary from _get_information_from_user() function
        :return: The same dictionary with corrected data format
        """
        for key, value in data.items():
            if key == 'month':
                continue
            data[key] = int(value)

        return data

    @staticmethod
    def _calculate_payout(data: dict) -> dict:
        """
        Payout calculation based on user values
        :param data: Prepared dictionary with integers data format
        :return: Dictionary with added payout
        """
        payout = data['income'] - data['vat'] - data['tax'] - data['zus']
        data['payout'] = payout

        return data


cmd = CommandLine()
cmd.prepare_data_for_one_month()
