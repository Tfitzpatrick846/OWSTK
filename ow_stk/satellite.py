from . import graphics as gfx
import comtypes
from comtypes.gen import STKUtil, STKObjects


def add(sc, name, apogee, perigee, inc, raan, trueAnomaly, argper=0):
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

def graphics(sat, profile):

    g = sat.Graphics
    g.SetAttributesType(STKObjects.eAttributesBasic)
    attributes = g.Attributes
    attributes2 = attributes.QueryInterface(STKObjects.IAgVeGfxAttributesOrbit)
    attributes2.Line.Width = 1
    attributes2.Line.Style = 0
    attributes2.Inherit = False
    attributes2.Color = gfx.colorProfile(profile)
    attributes2.MarkerStyle = 'Circle'
    attributes2.LabelVisible = False

    return g

