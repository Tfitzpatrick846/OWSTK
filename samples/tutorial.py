"""owstk tutorial"""

# import the necessary packages
import owstk
import comtypes
from comtypes.gen import STKUtil, STKObjects
from matplotlib import pyplot as plt
import numpy as np

print('First, open STK using the STKLicenseUsage.hta')
print('You will need STK Pro and STK Integration')

print('Establish a connection to the open application')
app = owstk.stk.app()

print('Get a root instance')
root = owstk.stk.root(app)

print('Open a new, untitled scenario')
sc = owstk.stk.newScenario(root)

print('Create a few satellites from the SS3 constellation')
satellites = owstk.oneweb.gen1.addSS3Constellation(sc, [0, 1, 410])
sat = satellites[0]

print('Create a few of the SNPs')
facilities = owstk.oneweb.gen1.addSNPs(sc, [4, 10])
fac = facilities[0] 

print('Add the Ku antennas to one of the satellites')
fixedSensors = owstk.oneweb.gen1.attachUserAntennas(sat)
fixedSensor = fixedSensors[0]

print('Add the Ka antennas to that same satellite')
targetedSensor = owstk.oneweb.gen1.attachGatewayAntenna(sat, fac)


print('\nTo exit, take the following steps:')
print('\t1) Delete all variables except for app')
print('\t2) Run app.quit()')
print('\t3) Close Python')
