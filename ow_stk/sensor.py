from . import graphics as gfx
import comtypes
from comtypes.gen import STKUtil, STKObjects

def add(obj, name, shape, dim1, dim2, az = 0, el = 90):

    sensor = obj.Children.New(STKObjects.eSensor, name)
    sensor2 = sensor.QueryInterface(STKObjects.IAgSensor)

    # set pointing
    sensor2.SetPointingType(STKObjects.eSnPtFixed)
    sensor2.CommonTasks.SetPointingFixedAzEl(az, el, STKObjects.eBoresightHold)

    # set beam shape
    if shape.lower().strip() == 'elipse':

        sensor2.SetPatternType(STKObjects.eSnComplexConic)
        minAngle = 0
        maxAngle = 360
        sensor2.CommonTasks.SetPatternComplexConic(dim1, dim2, minAngle, maxAngle)

    elif shape.lower().strip() == 'rectangle':

        sensor2.SetPatternType(STKObjects.eSnRectangular)
        sensor2.CommonTasks.SetPatternRectangular(dim1, dim2)

    else:

        raise ValueError('Unsupported sensor pattern')
    
    return sensor
