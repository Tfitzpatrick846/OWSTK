"""STK program and scenario interaction"""

import comtypes
from comtypes.client import  GetActiveObject
from comtypes.gen import STKUtil, STKObjects
import datetime
import psutil

def app():
    """Create the STK Application object.

    If STK is open, use that instance.  If not, open the license selector.
    """

    try:
        a = GetActiveObject('STK11.Application')
    except OSError:
        raise ProcessLookupError('STK is not running.  Open it using the STKLicenseUsage tool.')

    return a

def quit(app):
    """Quit STK."""

    app.quit()

    # kill the open process to disconnect from license server
    for p in psutil.process_iter(attrs=['name']):
        if p.info['name'] == 'AgUiApplication.exe':
            p.kill()

def root(app):
    """Get the root of the app and initialize units."""

    r = app.Personality2
    r.UnitPreferences.Item('LatitudeUnit').SetCurrentUnit('deg')
    r.UnitPreferences.Item('LongitudeUnit').SetCurrentUnit('deg')
    return r

def newScenario(root, name='Untitled'):
    """Create a new scenario."""

    root.NewScenario(name)
    return root.CurrentScenario

def clear(sc):
    """Delete all objects from scenario.
    """

    allChildren = sc.Children
    for k in range(allChildren.count):
        allChildren.item(0).unload()

def setTimePeriod(sc, startTime, stopTime):
    """Set the simulation start and stop times

    Start and stop times are specified as datetime objects from the datetime module.
    
    import datetime
    startTime = datetime.datetime.(year, month, day, hour, minute, second, microsecond)
    deltaTime = datetime.deltatime(days=365)
    stopTime = startTime + deltaTime
    setTImePeriod(sc, startTime, stopTime)
    """

    sc2 = sc.QueryInterface(STKObjects.IAgScenario)
    startTimeStr = datetime2str(startTime)
    stopTimeStr = datetime2str(stopTime)
    sc2.SetTimePeriod(startTimeStr, stopTimeStr)

def startTime(sc):
    t = sc.QueryInterface(STKObjects.IAgScenario).StartTime
    return str2datetime(t)

def stopTime(sc):
    t = sc.QueryInterface(STKObjects.IAgScenario).StopTime
    return str2datetime(t)

def datetime2str(time):
    """Convert datetime object to STK style time stamp."""

    def datetime2str1(time):
        """Only accepts datetime objects"""

        day = '%d' % time.day
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month = months[time.month - 1]
        year = '%04d' % time.year
        hour = '%02d' % time.hour
        minute = '%02d' % time.minute
        second = '%02d' % time.second
        millisecond = '%03d' % (time.microsecond/1000)
        return day + ' ' + month + ' ' + year + ' ' + hour + ':' + minute + ':' + second + '.' + millisecond

    if type(time) is list:

        strings=[]
        for k in range(len(time)):
            strings.append(datetime2str1(time[k]))

        return strings

    elif type(time) is tuple:

        strings=[]
        for k in range(len(time)):
            strings.append(datetime2str1(time[k]))

        return tuple(strings)

    else:

        return datetime2str1(time)

def str2datetime(string):
    """Convert STK style time stamp to datetime object."""

    def str2datetime1(string):
        """Only accepts strings"""

        parts = string.split(' ')
        day = int(float(parts[0]))
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month = months.index(parts[1]) + 1
        year = int(float(parts[2]))
        time = parts[3]
        hour = int(float(time[0:2]))
        minute = int(float(time[3:5]))
        second = int(float(time[6:8]))
        millisecond = int(float(time[9:12]))

        return datetime.datetime(year, month, day, hour, minute, second, 1000*millisecond)

    if type(string) is list:

        times=[]
        for k in range(len(string)):
            times.append(str2datetime1(string[k]))

        return times

    elif type(string) is tuple:

        times=[]
        for k in range(len(string)):
            times.append(str2datetime1(string[k]))

        return tuple(times)

    else:

        return str2datetime1(string)


def parentScenario(obj):

    while obj.ClassName != 'Scenario':
        obj = obj.Parent

    return obj
