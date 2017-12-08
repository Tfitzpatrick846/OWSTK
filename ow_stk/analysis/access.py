import comtypes
from comtypes.gen import STKUtil, STKObjects


def compute(fromObj, toObj):
    
    access = fromObj.GetAccessToObject(toObj)
    access.ComputeAccess()
    return access
