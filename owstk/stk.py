"""STK program and scenario interaction"""

import comtypes
from comtypes.client import  GetActiveObject
from comtypes.gen import STKUtil, STKObjects
import datetime

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
    del app

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
    r = root(sc)
    r.Rewind()

def startTime(sc):
    t = sc.QueryInterface(STKObjects.IAgScenario).StartTime
    return str2datetime(t)

def stopTime(sc):
    t = sc.QueryInterface(STKObjects.IAgScenario).StopTime
    return str2datetime(t)

def datetime2str(time):
    day = '%d' % time.day
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month = months[time.month - 1]
    year = '%04d' % time.year
    hour = '%02d' % time.hour
    minute = '%02d' % time.minute
    second = '%02d' % time.second
    millisecond = '%03d' % (time.microsecond/1000)
    return day + ' ' + month + ' ' + year + ' ' + hour + ':' + minute + ':' + second + '.' + millisecond

def str2datetime(string):

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

def parentScenario(obj):

    while obj.ClassName != 'Scenario':
        obj = obj.Parent

    return obj
