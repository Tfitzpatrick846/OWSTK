import comtypes
from comtypes.gen import STKUtil, STKObjects


def fromTo(fromObj, toObj):
    
    access = fromObj.GeAccsesToObject(toObj)
    access.ComputeAccess()
    
