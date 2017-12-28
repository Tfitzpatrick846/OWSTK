import comtypes
from comtypes.gen import STKUtil, STKObjects

def geoExclusion(obj, deg):
    """Add the GEO arc exclusion constraint.
    
    Useable for the following objects:
        sensor, attached to facility
    """

    cstr = obj.AccessConstraints.AddConstraint(STKObjects.eCstrGeoExclusion)
    cstr.Angle = deg;

    return cstr

def elevation(obj, minimum=None, maximum=None):
    """Add the elevation constraint.
    
    Useable for the following objects:
        sensor
        satellite
        facility
    """

    cstr = obj.AccessConstraints.AddConstraint(STKObjects.eCstrElevationAngle)
    
    if minimum is not None:
        cstr.EnableMin = True
        cstr.Min = minimum
    else:
        cstr.EnableMin = False

    if maximum is not None:
        cstr.EnableMax = True
        cstr.Max = maximum
    else:
        cstr.EnableMax = False

    return cstr

