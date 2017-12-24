from . import dataProvider as dp

def ecc(sat, startTime=None, stopTime=None, dt=60):
    """Get eccentricity array from satellite over given time"""

    dataPath = 'Parameter Set: Orbit/Orbit'
    dataName = 'Classical.Eccentricity'
    return dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
