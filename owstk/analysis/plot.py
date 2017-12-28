"""Plot results"""

from matplotlib import pyplot as plt
import datetime

def timePlot(time, values):

    plt.plot_date(time, values)
    plt.show()
