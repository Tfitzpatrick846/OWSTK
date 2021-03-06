"""OneWeb's Gen-1 system"""

from .. import satellite as stk_sat
from .. import sensor as stk_sensor
from .. import graphics
from .. import facility
import xlrd

import pkg_resources
resource_package = __name__
snpListFilename = pkg_resources.resource_filename(resource_package,'SNP sites v3.2.xlsx')

def addSS1Constellation(sc, satIDs=None):
    """Add OneWeb SS1 constellation to the scenario.

    Keyword arguments:
    sc -- scenario
    satIDs -- Optional parameter to specify which satellites should be added.
            A 4 digit number or string thereof, or list of those, to identify plane and
            sat number. For instance, 1208 is the 8th satellite in the 12th plane
            (default: all satellites)
    """

    return _addConstellation(sc, 9, 32, satIDs)

def addSS2Constellation(sc, satIDs=None):
    """Add OneWeb SS2 constellation to the scenario.

    Keyword arguments:
    sc -- scenario
    satIDs -- Optional parameter to specify which satellites should be added.
            A 4 digit number or string thereof, or list of those, to identify plane and
            sat number. For instance, 1208 is the 8th satellite in the 12th plane
            (default: all satellites)
    """

    return _addConstellation(sc, 18, 36, satIDs)

def addSS3Constellation(sc, satIDs=None):
    """Add OneWeb SS3 constellation to the scenario.

    Keyword arguments:
    sc -- scenario
    satIDs -- Optional parameter to specify which satellites should be added.
            A 4 digit number or string thereof, or list of those, to identify plane and
            sat number. For instance, 1208 is the 8th satellite in the 12th plane
            (default: all satellites)
    """

    return _addConstellation(sc, 18, 49, satIDs)

def _addConstellation(sc, numPlanes, numSatsPerPlane, satIDs):
    """Add OneWeb constellation to the scenario."""

    def createSatellite(sc, plane, sat, sma, ecc, inc, raan):

        trueAnomaly = sat * 360 / numSatsPerPlane
        satName = 'OneWeb%02d%02d' % (plane, sat)
        satObj = stk_sat.add(sc, satName, sma, ecc, inc, raan, trueAnomaly)
        stk_sat.graphics(satObj, graphics.OneWeb)
        return satObj

    sma = [
        7621,
        7581,
        7617,
        7577,
        7613,
        7573,
        7609,
        7569,
        7605,
        7565,
        7601,
        7562,
        7597,
        7557,
        7593,
        7553,
        7589,
        7585]
    inc = 87.9


    if satIDs is None:
        #add all satellites

        satObjs = []

        for plane in range(numPlanes):

            raan = 0 + plane * 180 / numPlanes
            sma1 = sma[plane]

            for sat in range(numSatsPerPlane):

                ecc = stk_sat.frozenEcc(sma1, inc)
                satObj = createSatellite(sc, plane, sat, sma1, ecc, inc, raan)
                satObjs.append(satObj)
                print('.',end='')

            print('\n')

        print('\n', end='')

        return satObjs

    elif type(satIDs) is list:
        # add the listed satellites

        satObjs = []

        for satID in satIDs:

            plane = int(satID/100)
            sma1 = sma[plane]
            ecc = stk_sat.frozenEcc(sma1, inc)
            sat = satID % 100
            raan = 0 + plane / numPlanes * 18 * 10.15
            satObj = createSatellite(sc, plane, sat, sma1, ecc, inc, raan)
            satObjs.append(satObj)
            print('.',end='')

        print('\n', end='')

        return satObjs

    else:
        # add the single satellite

        satID = satIDs

        plane = int(satID/100)
        sma1 = sma[plane]
        ecc = stk_sat.frozenEcc(sma1, inc)
        sat = satID % 100
        raan = 0 + plane * 180 / numPlanes
        satObj = createSatellite(sc, plane, sat, sma1, ecc, inc, raan)
        print('.',end='')

        print('\n', end='')

        return satObj

def addSNPs(sc, snpIDs=None):
    """Add the OneWeb SNP sites to the scenario.

    IDs are integers in the order of rollout.
    If no IDs are provided, all are added.
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

    if type(snpIDs) is int:
        # add a single SNP

        snpID = snpIDs

        for k in range(len(label)):

            if k == snpID:

                f = facility.add(sc, label[k], lat[k], lon[k])
                print('.',end='')
                print('\n', end='')
                return f

    elif snpIDs == None:

        facilities = []

        for k in range(len(label)):

            facilities.append(facility.add(sc, label[k], lat[k], lon[k]))
            print('.',end='')

        print('\n', end='')

        return facilities

    else:
        # add list of SNPs

        facilities = []

        for k in range(len(label)):

            if k in snpIDs:

                facility1 = facility.add(sc, label[k], lat[k], lon[k])
                facilities.append(facility1)
                print('.',end='')

        print('\n', end='')

        return facilities

def attachUserAntennas(sat):
    """Attach Ku antennas to a satellite."""

    sensors = []
    dim1 = 23.7
    dim2 = 1.568

    for k in range(16):

        if k < 8:
            el = 90 + ((k-8) + 0.5) * 2 * dim2
            az = 0
        else:
            el = 90 - ((k-8) + 0.5) * 2 * dim2
            az = 180
        sensor = stk_sensor.addFixed(sat,'Ku%02d' % k, 'rectangle', dim1, dim2, az, el)
        sensors.append(sensor)
        print('.',end='')

    print('\n', end='')

    return sensors

def attachGatewayAntenna(sat, snps):
    """Attach Ka antennas to a satellite."""

    ang = 1
    sensor = stk_sensor.addTargeted(sat, 'GW', 'conic', ang, None, snps)
    return sensor

