from . import dataProvider as dp
def ecc(sat, startTime, stopTime, dt=60):
    """Get eccentricity array from satellite over given time"""

    dataPath = 'CalculateKeplOrbit/Orbit'
    dataName = 'Classical.Eccentricity'
    return dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
