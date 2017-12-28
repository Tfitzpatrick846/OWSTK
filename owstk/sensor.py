"""Sensors"""

from . import graphics as gfx
import comtypes
from comtypes.gen import STKUtil, STKObjects

def addFixed(obj, name, shape, dim1, dim2, az = 0, el = 90):
    """Add a fixed antenna to an object."""

    def add1Fixed(obj, name, shape, dim1, dim2, az, el):
        sensor = obj.Children.New(STKObjects.eSensor, name)
        sensor2 = sensor.QueryInterface(STKObjects.IAgSensor)

        # set pointing
        sensor2.SetPointingType(STKObjects.eSnPtFixed)
        sensor2.CommonTasks.SetPointingFixedAzEl(az, el, STKObjects.eBoresightHold)

        # set beam shape
        if shape.lower().strip() == 'conic':

            sensor2.SetPatternType(STKObjects.eSnSimpleConic)
            sensor2.CommonTasks.SetPatternSimpleConic(dim1, 0.1)

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
    """Add a targeted antenna to an object."""

    def add1Targeted(obj, name, shape, dim1, dim2, targets):

        sensor = obj.Children.New(STKObjects.eSensor, name)
        sensor2 = sensor.QueryInterface(STKObjects.IAgSensor)

        # set pointing
        if type(targets) is not list:
            targets = [targets]

        sensor2.SetPointingType(STKObjects.eSnPtTargeted)
        pointing = sensor2.Pointing.QueryInterface(STKObjects.IAgSnPtTargeted)
        for target in targets:
            pointing.Targets.Add(target.Path)

        # set beam shape
        if shape.lower().strip() == 'conic':

            sensor2.SetPatternType(STKObjects.eSnSimpleConic)
            sensor2.CommonTasks.SetPatternSimpleConic(dim1, 0.1)

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

