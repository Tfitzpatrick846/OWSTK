"""Plot results"""

from matplotlib import pyplot as plt
from matplotlib.dates import date2num
import datetime

def timePlot(time, values):

    pyplotdate = _datetime2pyplotdate(time)
    fig, ax = plt.subplots()
    plt.plot_date(pyplotdate, values, '-')
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    plt.tight_layout()
    plt.show()

def intervals(intrvls):

    times = []
    val = []
    for intrvl in intrvls:

        times.append(intrvl[0])
        val.append(0)

        times.append(intrvl[0])
        val.append(1)

        times.append(intrvl[1])
        val.append(1)
    
        times.append(intrvl[1])
        val.append(0)
    
    fig, ax = plt.subplots()
    pyplotdate = _datetime2pyplotdate(times)
    plt.plot_date(pyplotdate, val, '-')
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    plt.tight_layout()
    plt.show()

def _datetime2pyplotdate(time):
    """Convert datetime value to something useable by pyplot.plot_date"""

    if (type(time) is list) or (type(time) is tuple):

        pyplotdate = []

        for k in range(len(time)):
            
            pyplotdate.append(date2num(time[k]))

    else:

        pyplotdate = date2num(time[k])

    return pyplotdate
