"""Orbital dynamics computations"""

from . import dataProvider as dp

def ecc(sat, startTime=None, stopTime=None, dt=60):
    """Get eccentricity array from satellite over given time"""

    dataPath = 'Parameter Set: Orbit/Orbit'
    dataName = 'Classical.Eccentricity'
    e = dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
    t = dp.timeVar(sat, dataPath, 'Time', startTime, stopTime, dt)
    return (t, e)

def x(sat, startTime=None, stopTime=None, dt=60):
    """Get x position array from satellite over given time"""

    dataPath = 'Parameter Set: Orbit/Orbit'
    dataName = 'Cartesian.X'
    x1 = dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
    t = dp.timeVar(sat, dataPath, 'Time', startTime, stopTime, dt)
    return (x1, t)

def y(sat, startTime=None, stopTime=None, dt=60):
    """Get y position array from satellite over given time"""

    dataPath = 'Parameter Set: Orbit/Orbit'
    dataName = 'Cartesian.Y'
    y1 = dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
    t = dp.timeVar(sat, dataPath, 'Time', startTime, stopTime, dt)
    return (y1, t)

def z(sat, startTime=None, stopTime=None, dt=60):
    """Get z position array from satellite over given time"""

    dataPath = 'Parameter Set: Orbit/Orbit'
    dataName = 'Cartesian.Z'
    z1 = dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
    t = dp.timeVar(sat, dataPath, 'Time', startTime, stopTime, dt)
    return (z1, t)

def sma(sat, startTime=None, stopTime=None, dt=60):
    """Get sma array from satellite over given time"""

    dataPath = 'Parameter Set: Orbit/Orbit'
    dataName = 'Classical.SemimajorAxis'
    s = dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
    t = dp.timeVar(sat, dataPath, 'Time', startTime, stopTime, dt)
    return (s, t)

def inc(sat, startTime=None, stopTime=None, dt=60):
    """Get inclination array from satellite over given time"""

    dataPath = 'Parameter Set: Orbit/Orbit'
    dataName = 'Classical.Inclination'
    s = dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
    t = dp.timeVar(sat, dataPath, 'Time', startTime, stopTime, dt)
    return (s, t)

def raan(sat, startTime=None, stopTime=None, dt=60):
    """Get RAAN array from satellite over given time"""

    dataPath = 'Parameter Set: Orbit/Orbit'
    dataName = 'Classical.RAAN'
    r = dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
    t = dp.timeVar(sat, dataPath, 'Time', startTime, stopTime, dt)
    return (r, t)

def perigee(sat, startTime=None, stopTime=None, dt=60):
    """Get perigee array from satellite over given time"""

    dataPath = 'Parameter Set: Orbit/Orbit'
    dataName = 'Classical.RadiusOfPeriapsis'
    r = dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
    t = dp.timeVar(sat, dataPath, 'Time', startTime, stopTime, dt)
    return (r, t)

def apogee(sat, startTime=None, stopTime=None, dt=60):
    """Get apogee array from satellite over given time"""

    dataPath = 'Parameter Set: Orbit/Orbit'
    dataName = 'Classical.RadiusOfApoapsis'
    r = dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
    t = dp.timeVar(sat, dataPath, 'Time', startTime, stopTime, dt)
    return (r, t)

def longitudeOfPerigee(sat, startTime=None, stopTime=None, dt=60):
    """Get perigee array from satellite over given time"""

    dataPath = 'Parameter Set: Orbit/Orbit'
    dataName = 'Classical.LongitudeOfPeriapsis'
    l = dp.timeVar(sat, dataPath, dataName, startTime, stopTime, dt)
    t = dp.timeVar(sat, dataPath, 'Time', startTime, stopTime, dt)
    return (l, t)

