from win32api import GetSystemMetrics
import comtypes
from comtypes.client import CreateObject, GetActiveObject

def app():
    try:
        a = GetActiveObject('STK11.Application')
    except OSError:
        a = CreateObject('STK11.Application')
        a.Visible = True
        a.UserControl = True

    return a

def quit(app):
    # app = app()
    app.quit()
    del app

def maximize(app):
    # width and height are wrong
    app.Top = 0
    app.Left = 0
    app.Width = int(GetSystemMetrics(0)/2)
    app.Height = int(GetSystemMetrics(1)-30)

def root(app):
    r = app.Personality2
    r.UnitPreferences.Item('LatitudeUnit').SetCurrentUnit('deg')
    r.UnitPreferences.Item('LongitudeUnit').SetCurrentUnit('deg')
    return r

def newScenario(root, name='Untitled'):
    root.NewScenario(name)
    return root.CurrentScenario

def new(name='Untitled'):
    a = app()
    r = root(a)
    sc = newScenario(r, name)
    return sc, r, a

def current():
    a = app()
    r = root(a)
    sc = root.CurrentScenario
    return sc, r, a

def clear(sc):
    allChildren = sc.Children
    for k in range(allChildren.count):
        allChildren.item(k).unload()
