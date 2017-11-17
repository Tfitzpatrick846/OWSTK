from win32api import GetSystemMetrics
from IPython.display import Image, display, SVG
import os as os
import comtypes
from comtypes.client import CreateObject, GetActiveObject
from comtypes.gen import STKUtil, STKObjects

try:
    from comtypes.gen import STKUtil, STKObjects
except NameError:
    pass

def stk():
    try:
        app = GetActiveObject('STK11.Application')
    except OSError:
        app = CreateObject('STK11.Application')
        app.Visible = True
        app.UserControl = True

    return app

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
    return r

def newScenario(root, name='Untitled'):
    root.NewScenario(name)
    return root.CurrentScenario

def addSat(sc, name, apogee, perigee, inc, raan, trueAnomaly, argper=0):
    # create the satellite object
    sat = sc.Children.New(STKObjects.eSatellite, name)
    
    # create the interface
    sat2 = sat.QueryInterface(STKObjects.IAgSatellite)

    # set the propagator
    sat2.SetPropagatorType(STKObjects.ePropagatorJ2Perturbation)
    satProp = sat2.Propagator
    satProp = satProp.QueryInterface(STKObjects.IAgVePropagatorJ2Perturbation)

    # switch the orbit representation to keplerian
    keplerian = satProp.InitialState.Representation.ConvertTo(STKUtil.eOrbitStateClassical)
    keplerian2 = keplerian.QueryInterface(STKObjects.IAgOrbitStateClassical)
    keplerian2.SizeShapeType = STKObjects.eSizeShapeAltitude
    keplerian2.LocationType = STKObjects.eLocationTrueAnomaly
    keplerian2.SizeShape.PerigeeAltitude = apogee
    keplerian2.SizeShape.ApogeeAltitude = perigee
    keplerian2.Orientation.Inclination = inc
    keplerian2.Orientation.ArgOfPerigee = argper
    keplerian2.Orientation.AscNode.Value = raan
    keplerian2.Location.Value = trueAnomaly

    satProp.InitialState.Representation.Assign(keplerian)
    satProp.Propagate()

    return sat2

def setSatGraphics(sat, profile):

    if profile == 0:
        color = '00FFFF'
    elif profile == 1:
        color = 'FF00FF'
    elif profile == 2:
        color = 'FFFF00'
    else:
        color = 'FFFFFF'

    graphics = sat.Graphics
    graphics.SetAttributesType(STKObjects.eAttributesBasic)
    attributes = graphics.Attributes
    attributes2 = attributes.QueryInterface(STKObjects.IAgVeGfxAttributesOrbit)
    attributes2.Line.Width = 1
    attributes2.Line.Style = 0
    attributes2.Inherit = False
    attributes2.Color = hexColorToInt(color)
    attributes2.MarkerStyle = 'Circle'
    attributes2.LabelVisible = False

    return graphics

def addFacility(sc, name, lat, lon):
    facility = sc.Children.New(STKObjects.eFacility, name)
    facility2 = facility.QueryInterface(STKObjects.IAgFacility)
    facility2.Position.AssignGeodetic(lat, lon, 0)
    return facility2

def hexColorToInt(rgb):

    r = int(rgb[0:2],16)
    g = int(rgb[2:4],16)
    b = int(rgb[4:6],16)

    color = format(b, '02X') + format(g, '02X') + format(r, '02X')

    return int(color,16) # STK uses BGR color codes
