import comtypes
from comtypes.client import CreateObject

app = CreateObject('STK11.Application')
root = app.Personality2

app.quit()
