"""
This script runs the tests for long range dependence from the module
test_long_range_parallel for the synthetic FARIMA time series
"""
import numpy as np
import os
import pandas as pd
import pickle

from test_long_range_parallel import absolutevalue
from test_long_range_parallel import variance
from test_long_range_parallel import variance_moulines
from test_long_range_parallel import varianceresiduals
from test_long_range_parallel import RSstatistic
from test_long_range_parallel import periodogram

dirname = '../data/FARIMA/'
files = ['series_1_1', 'series_1_2', 'series_1_3', 'series_1_4', 'series_1_5', \
         'series_2_1', 'series_2_2', 'series_2_3', 'series_2_4', 'series_2_5', \
         'series_3_1', 'series_3_2', 'series_3_3', 'series_3_4', 'series_3_5', \
         'series_4_1', 'series_4_2', 'series_4_3', 'series_4_4', 'series_4_5', \
         'series_5_1', 'series_5_2', 'series_5_3', 'series_5_4', 'series_5_5', \
         'series_6_1', 'series_6_2', 'series_6_3', 'series_6_4', 'series_6_5', \
         'series_7a_1', 'series_7a_2', 'series_7a_3', 'series_7a_4', \
         'series_7b_1', 'series_7b_2', \
         'series_8a_1', 'series_8a_2', 'series_8a_3', 'series_8a_4', \
         'series_8b_1', 'series_8b_2', \
         'series_9_1', 'series_9_2', 'series_9_3', 'series_9_4', \
         'series_10_1', 'series_10_2', 'series_10_3', 'series_10_4']

# Create pandas dataframe to store the results
df = pd.DataFrame(data={'series': files})

# Store time series into pickle files
for i in range(0, len(files)):
    ts = np.loadtxt(dirname + files[i] + '.txt')
    pickle.dump([0, 0, 0, ts], open(dirname + files[i] + '.pkl', 'wb'))

# Aggregation sizes
# For size 10000
#m = np.array([4, 5, 7, 9, 12, 15, 20, 25, 33, 42, 54, 70, 90, 115, 148, \
#    190, 244, 314], dtype=int)
# For size 852
m = np.array([4, 5, 7, 9, 12, 15, 20, 25, 33], dtype=int)

# Number of blocks for R/S method
K = 5

# Time step for the periodogram method
dt = 1.0

# Absolute value method
newpath = 'absolutevalue' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

H_absval = np.zeros(len(files))

for i in range(0, len(files)):
    H_absval[i] = absolutevalue(dirname, files[i], m)

df['H_absval'] = H_absval

# Variance method
newpath = 'variance' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

d_var = np.zeros(len(files))

for i in range(0, len(files)):
    d_var[i] = variance(dirname, files[i], m)

df['d_var'] = d_var

# Variance method (from Moulines's paper)
newpath = 'variancemoulines' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

H_varm = np.zeros(len(files))

for i in range(0, len(files)):
    H_varm[i] = variance_moulines(dirname, files[i], m)

df['H_varm'] = H_varm

# Variance of residuals method
newpath = 'varianceresiduals' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

d_varres = np.zeros(len(files))

for i in range(0, len(files)):
    d_varres[i] = varianceresiduals(dirname, files[i], m, 'mean')

df['d_varres'] = d_varres

# R/S method
newpath = 'RS' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

d_RS = np.zeros(len(files))

for i in range(0, len(files)):
    d_RS[i] = RSstatistic(dirname, files[i], m, K)

df['d_RS'] = d_RS

# Periodogram method
newpath = 'periodogram'
if not os.path.exists(newpath):
    os.makedirs(newpath)

d_p = np.zeros(len(files))

for i in range(0, len(files)):
    d_p[i] = periodogram(dirname, files[i], dt)

df['d_p'] = d_p

# Save dataframe into file
filename = 'FARIMA.pkl'
pickle.dump([df], open(filename, 'wb'))
