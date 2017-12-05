from . import satellite as stk_sat
from . import sensor as stk_sensor
from . import graphics
from . import facility
import xlrd

import pkg_resources
resource_package = __name__
snpListFilename = pkg_resources.resource_filename(resource_package,'SNP sites v3.2.xlsx')

def addSS3Constellation(sc):

    print('Creating OneWeb constellation')
    
    alt = 1200
    inc = 87.9
    numPlanes = 18
    numSatsPerPlane = 49

    satObjs = []

    for plane in range(numPlanes):

        raan = 0 + plane * 360 / numPlanes

        for sat in range(numSatsPerPlane):

            trueAnomaly = sat * 360 / numSatsPerPlane
            satName = 'OneWeb%02d%02d' % (plane, sat)
            satObj = stk_sat.add(sc, satName, alt, alt, inc, raan, trueAnomaly)
            stk_sat.graphics(satObj, graphics.OneWeb)
            satObjs.append(satObj)
            print('.',end='')
    
    return satObjs

def addSS2Constellation(sc):

    print('Creating OneWeb constellation')
    
    alt = 1200
    inc = 87.9
    numPlanes = 18
    numSatsPerPlane = 36

    satObjs = []

    for plane in range(numPlanes):

        raan = 0 + plane * 360 / numPlanes

        for sat in range(numSatsPerPlane):

            trueAnomaly = sat * 360 / numSatsPerPlane
            satName = 'OneWeb%02d%02d' % (plane, sat)
            satObj = stk_sat.add(sc, satName, alt, alt, inc, raan, trueAnomaly)
            stk_sat.graphics(satObj, graphics.OneWeb)
            satObjs.append(satObj)
            print('.',end='')
    
    return satObjs

def addSS1Constellation(sc):

    print('Creating OneWeb constellation')
    
    alt = 1200
    inc = 87.9
    numPlanes = 9
    numSatsPerPlane = 32

    satObjs = []

    for plane in range(numPlanes):

        raan = 0 + plane * 360 / numPlanes

        for sat in range(numSatsPerPlane):

            trueAnomaly = sat * 360 / numSatsPerPlane
            satName = 'OneWeb%02d%02d' % (plane, sat)
            satObj = stk_sat.add(sc, satName, alt, alt, inc, raan, trueAnomaly)
            stk_sat.graphics(satObj, graphics.OneWeb)
            satObjs.append(satObj)
            print('.',end='')
    
    return satObjs

def addSNPs(sc):

    snpBook = xlrd.open_workbook(snpListFilename)
    snpSheet = snpBook.sheet_by_index(0)

    label = []
    lat = []
    lon = []

    for k in range(snpSheet.nrows):

        if type(snpSheet.cell_value(rowx=k, colx=0)) is float:
            label.append(snpSheet.cell_value(rowx=k, colx=1))
            lat.append(snpSheet.cell_value(rowx=k, colx=3))
            lon.append(snpSheet.cell_value(rowx=k, colx=4))

    for k in range(len(label)):

            facility.add(sc, label[k], lat[k], lon[k])

def attachUserAntennas(sat):

    sensors = []
    dim1 = 23.7
    dim2 = 1.568

    for k in range(16):

        el = ((k-8) + 0.5) * dim2
        sensor = stk_sensor.addFixed(sat,'Ku%2d' % k, 'rectangle', dim1, dim2, 0, el)
        sensors.append(sensor)

    return sensors

def attachGatewayAntennas(sat):

    pass
