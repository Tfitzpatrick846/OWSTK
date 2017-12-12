import comtypes
from comtypes.gen import STKUtil, STKObjects


def compute(fromObj, toObj):
    """Compute the access from one object to another object."""
    
    access = fromObj.GetAccessToObject(toObj)
    access.ComputeAccess()
    return access
