from .. import stk

def timeVar(obj, dataPath, dataName, startTime, stopTime, dt=60):

    dataProvider = obj.DataProviders \
        .GetDataPrvTimeVarFromPath(dataPath) \
        .Exec(startTime, stopTime, dt)
    # could potentially be sped up by using ExecElements

    return dataProvider.DataSets.GetDataSetByName(dataName).GetValues()

def fixed(obj, dataPath, dataName):
    
    dataProvider = obj.DataProviders \
        .GetDataPrvFixedFromPath(dataPath) \
        .Exec()

    return dataProvider.DataSets.GetDataSetByName(dataName).GetValues()

def interval(obj, dataPath, dataName, startTime, stopTime):
    
    dataProvider = obj.DataProviders \
        .GetDataPrvIntervalFromPath(dataPath) \
        .Exec(startTime, stopTime)

    return dataProvider.DataSets.GetDataSetByName(dataName).GetValues()
