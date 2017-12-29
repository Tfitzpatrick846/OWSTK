OneWeb STK Module
=================

A variety of people and groups within OneWeb use STK for analysis. 
Most of them rely on Python or MATLAB interfaces to automate the
setup or data collection and to then postprocess that data outside
of STK.  This project is an attempt to create a collaborative tool
for connecting to STK, defining objects, and performing analyses to
improve the connection between groups and reduce redundant effort.

owstk is a Python3 module.


Installation
------------

Python
''''''

You need Python 3.4 or later to run owstk. You can have multiple Python
versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3 like this

.. code-block::

    $ sudo apt-get install python3 python3-pip

For other Linux flavors, OS X, and Windows, packages are available at

  http://www.python.org/getit/

Most distributions of OS X and Windows come with Python preinstalled.

Prerequisities
''''''''''''''

Install the prerequisite packages with the command

.. code-block::

    $ pip install -r requirements.txt

Generate the comtypes used in STK by running

.. code-block::

    $ python genstkcomtypes.py

Use
---

Always open STK using the `STKLicenseUsage.hta` tool.  Select the
licenses that you need.  The following licenses are used in owstk:

- STK Professional Edition
- STK Integration
- Analysis Workbench

Check out the `tutorial.py` script for example uses.

Closing
'''''''

STK must always be closed from Python using owstk.stk.quit(app).
Not doing so risks creating a hanging license checkout that
requires a restart to the license server to clear.
