import comtypes
from comtypes.gen import STKUtil, STKObjects
from . import graphics as gfx


def add(sc, name, lat, lon):
    """Add a facility at a certain location."""

    facility = sc.Children.New(STKObjects.eFacility, name)
    facility2 = facility.QueryInterface(STKObjects.IAgFacility)
    facility2.Position.AssignGeodetic(lat, lon, 0)
    return facility

def graphics(facility, profile):
    """Set graphics of facility to a profile.
    
    graphics = owstk.facility.graphics(sat, owstk.graphics.OneWeb)
    """

    g = facility.Graphics
    g.Color = gfx.colorProfile(profile)
    g.LabelVisible = False
