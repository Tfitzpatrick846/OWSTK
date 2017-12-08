import comtypes
from comtypes.gen import STKUtil, STKObjects


def fromTo(fromObj, toObj):
    
    access = fromObj.GetAccessToObject(toObj)
    access.ComputeAccess()
    
