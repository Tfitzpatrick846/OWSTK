"""Data providers for analysis tools

Not meant for direct access by users"""

from .. import stk

def timeVar(obj, dataPath, dataName, startTime=None, stopTime=None, dt=60):

    sc = stk.parentScenario(obj)

    if startTime == None:
        startTime = stk.startTime(sc)

    if stopTime == None:
        stopTime = stk.stopTime(sc)

    startTime_str = stk.datetime2str(startTime)
    stopTime_str = stk.datetime2str(stopTime)

    dataProvider = obj.DataProviders \
        .GetDataPrvTimeVarFromPath(dataPath) \
        .Exec(startTime_str, stopTime_str, dt)
    # could potentially be sped up by using ExecElements

    return dataProvider.DataSets.GetDataSetByName(dataName).GetValues()

def fixed(obj, dataPath, dataName):
    
    dataProvider = obj.DataProviders \
        .GetDataPrvFixedFromPath(dataPath) \
        .Exec()

    return dataProvider.DataSets.GetDataSetByName(dataName).GetValues()

def interval(obj, dataPath, dataName, startTime=None, stopTime=None):
    
    sc = stk.parentScenario(obj)

    if startTime == None:
        startTime = stk.startTime(sc)

    if stopTime == None:
        stopTime = stk.stopTime(sc)

    startTime_str = stk.datetime2str(startTime)
    stopTime_str = stk.datetime2str(stopTime)

    dataProvider = obj.DataProviders \
        .GetDataPrvIntervalFromPath(dataPath) \
        .Exec(startTime_str, stopTime_str)

    return dataProvider.DataSets.GetDataSetByName(dataName).GetValues()
