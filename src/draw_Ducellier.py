"""
This script draws the results of the tests with the module draw_long_range
for the LFE catalog of Ducellier (2022)
"""
import numpy as np
import os
import pandas as pd

from draw_long_range import draw_absolutevalue
from draw_long_range import draw_variance
from draw_long_range import draw_variance_moulines
from draw_long_range import draw_varianceresiduals
from draw_long_range import draw_RSstatistic
from draw_long_range import draw_periodogram

# List of LFE families
templates = np.loadtxt('../data/Plourde_2015/templates_list.txt', \
    dtype={'names': ('name', 'family', 'lat', 'lon', 'depth', 'eH', \
    'eZ', 'nb'), \
         'formats': ('S13', 'S3', np.float, np.float, np.float, \
    np.float, np.float, np.int)}, \
    skiprows=1)

# Absolute value method
#for i in range(0, np.shape(templates)[0]):
#    filename = templates[i][0].astype(str)
#    draw_absolutevalue(filename)

#os.rename('absolutevalue', 'absolutevalue_Ducellier')

# Variance method
#for i in range(0, np.shape(templates)[0]):
#    filename = templates[i][0].astype(str)
#    draw_variance(filename)

#os.rename('variance', 'variance_Ducellier')

# Variance method (from Moulines's paper)
#for i in range(0, np.shape(templates)[0]):
#    filename = templates[i][0].astype(str)
#    draw_variance_moulines(filename)

#os.rename('variancemoulines', 'variancemoulines_Ducellier')

# Variance of residuals method
for i in range(0, np.shape(templates)[0]):
    filename = templates[i][0].astype(str)
    if i != 59:
        draw_varianceresiduals(filename, 'mean')

os.rename('varianceresiduals', 'varianceresiduals_Ducellier')

# R/S method
for i in range(0, np.shape(templates)[0]):
    filename = templates[i][0].astype(str)
    draw_RSstatistic(filename)

os.rename('RS', 'RS_Ducellier')

# Periodogram method
for i in range(0, np.shape(templates)[0]):
    filename = templates[i][0].astype(str)
    draw_periodogram(filename)

os.rename('periodogram', 'periodogram_Ducellier')
