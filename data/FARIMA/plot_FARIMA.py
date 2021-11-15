"""
This script plots the synthetic time series
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

from datetime import datetime, timedelta
from math import floor

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

true_d = [0.0, 0.1, 0.2, 0.3, 0.4, \
          0.0, 0.1, 0.2, 0.3, 0.4, \
          0.0, 0.1, 0.2, 0.3, 0.4, \
          0.0, 0.1, 0.2, 0.3, 0.4, \
          0.0, 0.1, 0.2, 0.3, 0.4, \
          0.0, 0.1, 0.2, 0.3, 0.4, \
          0.0, 0.1, 0.2, 0.3, \
          0.0, 0.1, \
          0.0, 0.1, 0.2, 0.3, \
          0.0, 0.1, \
          0.0, 0.1, 0.2, 0.3, \
          0.0, 0.1, 0.2, 0.3]

for i in range(0, len(files)):

    data = pickle.load(open(files[i] + '.pkl', 'rb'))
    X = data[3]
    plt.figure(1, figsize=(20, 10))
    plt.plot(np.arange(0, len(X)), X, 'k-')
    plt.xlim([-0.5, len(X) - 0.5])
    plt.xlabel('Time', fontsize=24)
    plt.ylabel('Value', fontsize=24)
    plt.title(files[i] + ' - d = {}'.format(true_d[i]), fontsize=24)
    plt.savefig(files[i] + '.eps', format='eps')
    plt.close(1)
