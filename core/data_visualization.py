import matplotlib.pyplot as plt
from core.finance import Finance


class DataVisualization(Finance):

    def __init__(self):
        super().__init__()

    def year_plot(self, year: int):
        """
        Show plot with whole year finance statistics
        :param year: The table name
        """
        columns = self.get_column_names(year)
        colors = ['dodgerblue', 'red', 'green', 'yellow', 'grey']
        x_axis = self.get_values_from_column(year, 'month')

        plt.figure(figsize=(15, 5))

        color_counter = 0
        for data in columns:
            if data == 'month':
                continue

            y_axis = self.get_values_from_column(year, data)
            y_axis = [float(y) for y in y_axis]
            plt.plot(x_axis, y_axis, colors[color_counter], label=data, linewidth=2)
            color_counter += 1

        # plot config
        plt.xlabel("Months", fontsize=16)
        plt.ylabel("Money", fontsize=16)
        plt.title(f"Finance in {year}", fontsize=16)
        plt.legend()
        plt.grid(True)

        plt.show()
        plt.clf()
        plt.close('all')

    def years_comparison(self):
        """ Show plot comparing the whole year payout summary """
        data = {}
        for table in self.get_table_names():
            year = int(table.removeprefix("YEAR_"))
            data[str(year)] = self.get_payout_summary_from_year(year)

        courses = list(data.keys())
        values = list(data.values())

        plt.figure(figsize=(8, 5))

        plt.bar(courses, values, color='dodgerblue', width=0.2)

        plt.xlabel("Years")
        plt.ylabel("Finances for the whole year")
        plt.title("Comparison of finances in years")
        plt.show()
