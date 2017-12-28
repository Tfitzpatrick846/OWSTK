"""Plot results"""

from matplotlib import pyplot as plt
import datetime

def timePlot(time, values):

    pyplotdate = _datetime2pyplotdate(time)
    plt.plot_date(pyplotdate, values)
    plt.show()

def _datetime2pyplotdate(time):
    """Convert datetime value to something useable by pyplot.plot_date"""

    refday = datetime.datetime(1,1,1)
    
    if (type(time) is list) or (type(time) is tuple):

        pyplotdate = []

        for k in range(len(time)):
            
            dt = time[k] - refday
            sec = dt.total_seconds()
            days = sec / (60*60*24)
            pyplotdate.append(days)
    else:

        dt = time - refday
        sec = dt.total_second()
        days = sec / (60*60*24)
        pyplotdate = days

    return pyplotdate
