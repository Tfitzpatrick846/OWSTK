from . import satellite as stk_sat
from . import graphics

def addConstellation(sc):

    print('Creating Telesat constellation')
    
    alt_pol = 1000
    inc_pol = 99.5
    numPlanes_pol = 3
    numSatsPerPlane_pol = 12

    for plane in range(numPlanes_pol):

        raan = 0 + plane * 63.2
        trueAnomalyOffset = 0

        for sat in range(numSatsPerPlane_pol):

            trueAnomaly = trueAnomalyOffset + sat * 360 / numSatsPerPlane_pol
            satName = 'Telesat_pol%02d%02d' % (plane, sat)
            satObj = stk_sat.add(sc, satName, alt_pol, alt_pol, inc_pol, raan, trueAnomaly)
            stk_sat.graphics(satObj, graphics.Telesat)
            print('.',end='')

    subPlane = 2

    for plane in range(subPlane):

        raan = 94.8 + plane * 63.2
        trueAnomalyOffset = 15

        for sat in range(numSatsPerPlane_pol):

            trueAnomaly = trueAnomalyOffset + sat * 360 / numSatsPerPlane_pol
            satName = 'Telesat_pol%02d%02d' % (numPlanes_pol + plane, sat)
            satObj = stk_sat.add(sc, satName, alt_pol, alt_pol, inc_pol, raan, trueAnomaly)
            stk_sat.graphics(satObj, graphics.Telesat)
            print('.',end='')

    for plane in range(1):

        raan = 31.6
        trueAnomalyOffset = 15

        for sat in range(numSatsPerPlane_pol):

            trueAnomaly = sat * 360 / numSatsPerPlane_pol
            satName = 'Telesat_pol%02d%02d' % (numPlanes_pol + 5, sat)
            satObj = stk_sat.add(sc, satName, alt_pol, alt_pol, inc_pol, raan, trueAnomaly)
            stk_sat.graphics(satObj, graphics.Telesat)
            print('.',end='')

    alt_inc = 1248
    inc_inc = 37.4
    numPlanes_inc = 5
    numSatsPerPlane_inc = 9

    for plane in range(numPlanes_inc):

        raan = 0 + plane * 72
        trueAnomalyOffset = 0

        for sat in range(numSatsPerPlane_inc):

            trueAnomaly = trueAnomalyOffset + sat * 360 / numSatsPerPlane_inc
            satName = 'Telesat_inc%02d%02d' % (plane, sat)
            satObj = stk_sat.add(sc, satName, alt_inc, alt_inc, inc_inc, raan, trueAnomaly)
            stk_sat.graphics(satObj, graphics.Telesat)
            print('.',end='')

