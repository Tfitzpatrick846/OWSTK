import comtypes
from comtypes.gen import STKUtil, STKObjects
from . import graphics as gfx


def add(sc, name, lat, lon):
    facility = sc.Children.New(STKObjects.eFacility, name)
    facility2 = facility.QueryInterface(STKObjects.IAgFacility)
    facility2.Position.AssignGeodetic(lat, lon, 0)
    return facility2

def graphics(facility, profile):

    g = facility.Graphics
    g.Color = gfx.colorProfile(profile)
    g.LabelVisible = False


