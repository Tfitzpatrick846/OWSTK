from . import satellite as stk_sat
from . import sensor as stk_sensor
from . import graphics
from . import facility
import xlrd

import pkg_resources
resource_package = __name__
snpListFilename = pkg_resources.resource_filename(resource_package,'SNP sites v3.2.xlsx')

def addSS1Constellation(sc, satIDs=[]):
    """ Build the OneWeb Service Stage 1 constellation with no spares
    sc: scenario
    satIDs: optional parameter to specify which satellites should be added
           list of 4 digit number or string thereof to identify plane and sat number
           for instance, 1208 is the 8th satellite in the 12th plane
    """

    print('Creating OneWeb constellation')
    
    return addConstellation(sc, 9, 32, satIDs)

def addSS2Constellation(sc, satIDs=[]):
    """ Build the OneWeb Service Stage 2 constellation with no spares
    sc: scenario
    satIDs: optional parameter to specify which satellites should be added
           list of 4 digit number or string thereof to identify plane and sat number
           for instance, 1208 is the 8th satellite in the 12th plane
    """

    print('Creating OneWeb constellation')
    
    return addConstellation(sc, 18, 36, satIDs)

def addSS3Constellation(sc, satIDs=[]):
    """ Build the OneWeb Service Stage 3 constellation with no spares
    sc: scenario
    satIDs: optional parameter to specify which satellites should be added
           list of 4 digit number or string thereof to identify plane and sat number
           for instance, 1208 is the 8th satellite in the 12th plane
    """

    print('Creating OneWeb constellation')
    
    return addConstellation(sc, 18, 49, satIDs)

def addConstellation(sc, numPlanes, numSatsPerPlane, satIDs):
    """Build a OneWeb constellation with a given number of planes and satellites
    """

    def createSatellite(sc, plane, sat, alt, inc, raan):

        trueAnomaly = sat * 360 / numSatsPerPlane
        satName = 'OneWeb%02d%02d' % (plane, sat)
        satObj = stk_sat.add(sc, satName, alt, alt, inc, raan, trueAnomaly)
        stk_sat.graphics(satObj, graphics.OneWeb)
        return satObj
    
    
    alt = 1200
    inc = 87.9

    satObjs = []

    if satIDs:

        for satID in satIDs:

            plane = int(satID/100)
            sat = satID % 100
            raan = 0 + plane * 180 / numPlanes
            satObj = createSatellite(sc, plane, sat, alt, inc, raan)
            satObjs.append(satObj)
            print('.',end='')

    else:

        for plane in range(numPlanes):

            raan = 0 + plane * 180 / numPlanes

            for sat in range(numSatsPerPlane):

                satObj = createSatellite(sc, plane, sat, alt, inc, raan)
                satObjs.append(satObj)
                print('.',end='')

            print('\n')

    return satObjs

def addSNPs(sc, snpIDs=[]):
    """ Add the OneWeb SNP sites
    If IDs are provided, the numbering is the order of the rollout
    """

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

    if not snpIDs:
        snpIDs = list(range(len(label)))

    for k in range(len(label)):

        if k in snpIDs:

            facility.add(sc, label[k], lat[k], lon[k])
            print('.',end='')

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
