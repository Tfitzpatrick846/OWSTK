import owstk
import comtypes
from comtypes.gen import STKUtil, STKObjects
from matplotlib import pyplot as plt
import numpy as np

if 'app' not in vars():
    app = owstk.stk.app()

if 'root' not in vars():
    root = owstk.stk.root(app)

if 'sc' not in vars():
    sc = owstk.stk.newScenario(root)

satellites = owstk.oneweb.gen1.addSS3Constellation(sc, [0, 1, 410])
sat = satellites[0]

facilities = owstk.oneweb.gen1.addSNPs(sc, [4, 10])
fac = facilities[0] 

fixedSensors = owstk.oneweb.gen1.attachUserAntennas(satellites[0])
fixedSensor = fixedSensors[0]

targetedSensor = owstk.oneweb.gen1.attachGatewayAntenna(sat, fac)
