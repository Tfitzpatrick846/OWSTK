"""Export data"""

from scipy.io import savemat

def mat(filename, mdict):
    """Export dictionary to .mat file for MATLAB"""

    savemat(filename, mdict)

