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

def startTime(sc):
    t = sc.QueryInterface(STKObjects.IAgScenario).StartTime
    return str2datetime(t)

def stopTime(sc):
    t = sc.QueryInterface(STKObjects.IAgScenario).StopTime
    return str2datetime(t)

def datetime2str(datetime):
    day = '%02d' % datetime.day
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month = months[datetime.month - 1]
    year = '%04d' % datetime.year
    hour = '%02d' % datetime.hour
    minute = '%02d' % datetime.minute
    second = '%02d' % datetime.second
    millisecond = '%03d' % (datetime.microsecond/1000)
    return day + ' ' + month + ' ' + year + ' ' + hour + ':' + minute + ':' + second + '.' + millisecond

def str2datetime(string):

    day = int(float(string[0:2]))
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_str = string[3:6]
    month = months.index(month_str) + 1
    year = int(float(string[7:11]))
    hour = int(float(string[12:14]))
    minute = int(float(string[15:17]))
    second = int(float(string[18:20]))
    millisecond = int(float(string[21:24]))

    return datetime.datetime(year, month, day, hour, minute, second, 1000*millisecond)

def parentScenario(obj):

    while obj.ClassName != 'Scenario':
        obj = obj.Parent

    return obj
