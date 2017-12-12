import comtypes
from comtypes.client import CreateObject, GetActiveObject
from comtypes.gen import STKUtil, STKObjects
import datetime

def app():
    """Create the STK Application object.

    If STK is open, use that instance.  If not, open STK.
    """

    try:
        a = GetActiveObject('STK11.Application')
    except OSError:
        a = CreateObject('STK11.Application')
        a.Visible = True
        a.UserControl = True

    return a

def quit(app):
    """Quit STK."""

    # app = app()
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

def new(name='Untitled'):
    """Create set of objects for a new scenario.

    Creates the application, root, and scenario objects.
    """

    a = app()
    r = root(a)
    sc = newScenario(r, name)
    return sc, r, a

def current():
    """Create set of objects for the current scenario.

    Creates the application, root, and scenario objects.
    """

    a = app()
    r = root(a)
    sc = root.CurrentScenario
    return sc, r, a

def clear(sc=None):
    """Delete all objects from scenario.

    If no scenario is provided, all objects in current scenario are deleted.
    """

    if sc == None:
        a = app()
        r = root(a)
        sc = r.CurrentScenario

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

    def datetime2str(dt):
        day = '%02d' % dt.day
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month = months[dt.month - 1]
        year = '%04d' % dt.year
        hour = '%02d' % dt.hour
        minute = '%02d' % dt.minute
        second = '%02d' % dt.second
        millisecond = '%03d' % (dt.microsecond/1000)
        return day + ' ' + month + ' ' + year + ' ' + hour + ':' + minute + ':' + second + '.' + millisecond

    sc2 = sc.QueryInterface(STKObjects.IAgScenario)
    startTimeStr = datetime2str(startTime)
    stopTimeStr = datetime2str(stopTime)
    sc2.SetTimePeriod(startTimeStr, stopTimeStr)

