"""Analysis workbench tools

Top level documentation can be found at
http://help.agi.com/stkdevkit/#DocX/AgSTKVgtLib~IAgCrdnProvider.html
"""

import comtypes
from comtypes.gen import STKObjects, AgSTKVgtLib
from .. import stk
import datetime

def angleBetween(vertex, obj1, obj2, startTime=None, stopTime=None, dt=60):
    """Angle between vectors from vertex to obj1 and vertex to obj2"""

    name = obj1.InstanceName + '-' \
        + vertex.InstanceName + '-' \
        + obj2.InstanceName
    if vertex.Vgt.Angles.Contains(name):
        angle = vertex.Vgt.Angles.Item(name)
    else:
        description = 'Angle between vectors from ' + vertex.InstanceName \
            + ' to ' + obj1.InstanceName + ' and ' \
            + vertex.InstanceName + ' to ' + obj2.InstanceName
        angle = vertex.Vgt.Angles.Factory.Create(name, description, 
            AgSTKVgtLib.eCrdnAngleTypeBetweenVectors)

    dl = dateList(startTime, stopTime, dt)

    a = []

    for date in dl:
        
        a.append(angle.FindAngle(stk.datetime2str(date)).Angle)

    return a, dl

    
def dateList(startTime=None, stopTime=None, dt=60):

    dl = []
    
    if startTime == None:
        startTime = stk.startTime(sc)

    if stopTime == None:
        stopTime = stk.stopTime(sc)
    
    dtdt = datetime.timedelta(seconds=dt)

    maxIter = int(1e8)
    if (stopTime - startTime)/dtdt > maxIter:
        raise MemoryError('Date list is too long')

    t = startTime

    while t <= stopTime:
        dl.append(t)
        t += dtdt

    return dl
