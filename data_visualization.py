import matplotlib.pyplot as plt
from finance import Finance


class DataVisualization(Finance):

    def __init__(self):
        super().__init__()

    def year_plot(self, year):
        """
        Show plot with whole year finance statistics
        :param year: The table name
        """
        columns = self.get_column_names(year)
        colors = ['dodgerblue', 'red', 'green', 'yellow', 'grey']
        x_axis = self.read_values_from_column(year, 'month')

        color_counter = 0
        for data in columns:
            if data == 'month':
                continue

            y_axis = self.read_values_from_column(year, data)
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
