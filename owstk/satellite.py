"""Satellites"""

from . import graphics as gfx
import comtypes
from comtypes.gen import STKUtil, STKObjects
import numpy as np

def add(sc, name, sma, ecc, inc, raan, trueAnomaly, argper=0):
    """Add a satellite."""

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

    # semimajor axis and eccentricity
    keplerian2.SizeShapeType = STKObjects.eSizeShapeSemimajorAxis
    sizeShape = keplerian2.SizeShape.QueryInterface(STKObjects.IAgClassicalSizeShapeSemimajorAxis)
    sizeShape.SemiMajorAxis = sma
    sizeShape.Eccentricity = ecc

    # inclination and argument of perigee
    keplerian2.Orientation.Inclination = inc
    keplerian2.Orientation.ArgOfPerigee = argper

    # ascending node
    keplerian2.Orientation.AscNodeType = STKObjects.eAscNodeRAAN
    ascNode = keplerian2.Orientation.AscNode.QueryInterface(STKObjects.IAgOrientationAscNodeRAAN)
    ascNode.Value = raan

    # true anomaly
    keplerian2.LocationType = STKObjects.eLocationTrueAnomaly
    location = keplerian2.Location.QueryInterface(STKObjects.IAgClassicalLocationTrueAnomaly)
    location.Value = trueAnomaly

    # assign the state and propagate
    satProp.InitialState.Representation.Assign(keplerian)
    propagate(sat)

    return sat

def graphics(sat, profile):
    """Set graphics of satellite to a profile.
    
    graphics = owstk.satellite.graphics(sat, owstk.graphics.OneWeb)
    """

    # create the interface
    sat2 = sat.QueryInterface(STKObjects.IAgSatellite)

    g = sat2.Graphics
    g.SetAttributesType(STKObjects.eAttributesBasic)
    attributes = g.Attributes
    attributes2 = attributes.QueryInterface(STKObjects.IAgVeGfxAttributesOrbit)
    attributes2.Line.Width = 1
    attributes2.Line.Style = 0 # 0: Solid
    attributes2.Inherit = False
    attributes2.Color = gfx.colorProfile(profile)
    attributes2.MarkerStyle = 'Circle'
    attributes2.LabelVisible = False

    return g

def propagate(sats):
    """Propagate satellite or list of satellites."""

    if type(sats) is not list:
        sats = [sats]

    for sat in sats: 
        # create the interface
        sat2 = sat.QueryInterface(STKObjects.IAgSatellite)

        # set the propagator
        satProp = sat2.Propagator
        satProp = satProp.QueryInterface(STKObjects.IAgVePropagatorJ2Perturbation)

        # propagate
        satProp.Propagate()

def frozenEcc(sma, inc):
    """Get the eccentricity for frozen orbit
    
    sma in km
    inc in deg
    """
    
    omega_f = np.pi/2 # argument of perigee
    ecc = 7.459335 * np.sin(inc * np.pi/180) * np.sin(omega_f) / (sma)
    return ecc

def apogee(sma, ecc):
    """Calculate the apogee from SMA and eccentricity"""

    return sma * (1 + ecc)

def perigee(sma, ecc):
    """Calculate the perigee from SMA and eccentricity"""

    return sma * (1 - ecc)
