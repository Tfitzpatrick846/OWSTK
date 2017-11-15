from win32api import GetSystemMetrics
from IPython.display import Image, display, SVG
import os as os
import comtypes
from comtypes.client import CreateObject, GetActiveObject

try:
   from comtypes.gen import STKUtil, STKObjects
except NameError:
   pass

def stk():
   try:
      app = GetActiveObject('STK11.Application')
   except OSError:
      app = CreateObject('STK11.Application')
      app.Visible = True
      app.UserControl = True

   return app

def quit(app):
   # app = app()
   app.quit()
   del app

def maximize(app):
   # width and height are wrong
   app.Top = 0
   app.Left = 0
   app.Width = int(GetSystemMetrics(0)/2)
   app.Height = int(GetSystemMetrics(1)-30)

def root(app):
   r = app.Personality2
   from comtypes.gen import STKUtil, STKObjects
   return r



