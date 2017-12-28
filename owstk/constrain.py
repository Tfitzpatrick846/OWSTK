"""Access constraints.

Find list of constraints here:
http://help.agi.com/stkdevkit/#DocX/STKObjects~IAgAccessConstraintCollection~AddConstraint.html
"""

import comtypes
from comtypes.gen import STKUtil, STKObjects

def geoExclusion(obj, deg):
    """Add the GEO arc exclusion constraint.
    
    Useable for the following objects:
        sensor, attached to facility
    """

    cnstr = _getcnstr(obj, STKObjects.eCstrGeoExclusion)
    cnstr.Angle = deg;

    return cnstr

def elevation(obj, minimum=None, maximum=None):
    """Add the elevation constraint.
    
    Useable for the following objects:
        sensor
        satellite
        facility
    """

    cnstr = _getcnstr(obj, STKObjects.eCstrElevationAngle)
    _minmaxcnstr(cnstr, minimum, maximum)
    return cnstr

def azimuth(obj, minimum=None, maximum=None):
    """Add the azimuth constraint.
    
    Useable for the following objects:
        sensor
        satellite
        facility
    """

    cnstr = _getcnstr(obj, STKObjects.eCstrElevationAngle)
    _minmaxcnstr(cnstr, minimum, maximum)
    return cnstr

def gndElevation(obj, minimum=None, maximum=None):
    """Add the ground elevation constraint.
    
    Useable for the following objects:
        sensor
        satellite
    """

    cnstr = _getcnstr(obj, STKObjects.eCstrGroundElevAngle)
    _minmaxcnstr(cnstr, minimum, maximum)
    return cnstr


def _minmaxcnstr(cnstr, minimum=None, maximum=None):
    """Set values of min/max constraint."""

    cnstr2 = cnstr.QueryInterface(STKObjects.IAgAccessCnstrMinMax)
    
    if minimum is not None:
        cnstr2.EnableMin = True
        cnstr2.Min = minimum
    else:
        cnstr2.EnableMin = False

    if maximum is not None:
        cnstr2.EnableMax = True
        cnstr2.Max = maximum
    else:
        cnstr2.EnableMax = False

    return cnstr2

def _getcnstr(obj, enum):
    """Get the constraint object"""

    ac = obj.AccessConstraints

    if ac.IsConstraintActive(enum):
        cnstr = ac.GetActiveConstraint(enum)
    else:
        cnstr = ac.AddConstraint(enum)

    return cnstr
