from . import graphics as gfx
import comtypes
from comtypes.gen import STKUtil, STKObjects

def addFixed(obj, name, shape, dim1, dim2, az = 0, el = 90):

    def add1Fixed(obj, name, shape, dim1, dim2, az, el):
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

    sensors = []

    if type(obj) is list:

        for k in range(len(obj)):

            sensor = add1Fixed(obj[k], name, shape, dim1, dim2, az, el)
            sensors.append(sensor)

    else:

        sensors = add1Fixed(obj, name, shape, dim1, dim2, az, el)

    return sensors

def addTargeted(obj, name, shape, dim1, dim2, targets):

    def add1Targeted(obj, name, shape, dim1, dim2, targets):
        sensor = obj.Children.New(STKObjects.eSensor, name)
        sensor2 = sensor.QueryInterface(STKObjects.IAgSensor)

        # set pointing
        sensor2.SetPointingType(STKObjects.eSnPtTargeted)
        sensor2.CommonTasks.SetPointingTargetedTracking(STKObjects.eTrackModeTranspond, STKObjects.eBoresightRotate, targets.Path)

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

    sensors = []

    if type(obj) is list:

        for k in range(len(obj)):

            sensor = add1Targeted(obj[k], name, shape, dim1, dim2, targets)
            sensors.append(sensor)

    else:

        sensors = add1Targeted(obj, name, shape, dim1, dim2, targets)

    return sensors

