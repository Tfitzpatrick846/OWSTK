from . import satellite as stk_sat
from . import graphics

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

