"""Access computations"""

import comtypes
from comtypes.gen import STKUtil, STKObjects
from ..stk import str2datetime, datetime2str

def compute(fromObj, toObj):
    """Compute the access from one object to another object."""
    
    access = fromObj.GetAccessToObject(toObj)
    access.ComputeAccess()
    return access

def intervals(access):
    """Compute access intervals and return as datetime pairs."""

    agIntervals = access.ComputedAccessIntervalTimes
    strIntervals = agIntervals.ToArray(0,-1)
    intervals = []
    for strInterval in strIntervals:
        intervals.append(str2datetime(strInterval))

    return tuple(intervals)
