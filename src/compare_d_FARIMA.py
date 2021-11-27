"""
This script compare the true value of the fractional parameter d
with the computed value for all the synthetic FARIMA time series
"""
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

method = 'periodogram'
column = 'd_p'

prefix = [['series_1', 'series_2', 'series_3', 'series_4', 'series_5', 'series_6'], \
          ['series_7a', 'series_7b', 'series_8a', 'series_8b', 'series_9', 'series_10']]

number_values = [[5, 5, 5, 5, 5, 5], [4, 2, 4, 2, 4, 4]]

true_alpha = np.array([0.0, 0.0, 0.0, 0.0, 0.0, \
                       0.0, 0.0, 0.0, 0.0, 0.0, \
                       0.0, 0.0, 0.0, 0.0, 0.0, \
                       0.0, 0.0, 0.0, 0.0, 0.0, \
                       0.0, 0.0, 0.0, 0.0, 0.0, \
                       0.0, 0.0, 0.0, 0.0, 0.0, \
                       1.5, 1.5, 1.5, 1.5, \
                       1.2, 1.2, \
                       1.5, 1.5, 1.5, 1.5, \
                       1.2, 1.2, \
                       1.5, 1.5, 1.5, 1.5, \
                       1.5, 1.5, 1.5, 1.5])

data = pickle.load(open('FARIMA.pkl', 'rb'))

data['H_absval'] = np.where(true_alpha > 0.0, data['H_absval'] - 1.0 / true_alpha, data['H_absval'] - 1.0 / 2.0)
data['H_varm'] = np.where(true_alpha > 0.0, data['H_varm'] - 1.0 / true_alpha, data['H_varm'] - 1.0 / 2.0)

xmin = - 0.01
xmax = 0.41
ymin = np.min(data.min()[1:]) - 0.01
ymax = np.max(data.max()[1:]) + 0.01

params = {'legend.fontsize': 24, \
          'xtick.labelsize':24, \
          'ytick.labelsize':24}
pylab.rcParams.update(params)
plt.figure(1, figsize=(30, 10))


for i in range(0, len(prefix)):
    for j in range(0, len(prefix[i])):
        ax = plt.subplot2grid((2, 6), (i, j))
        true_d = []
        computed_d = []
        for k in range(0, number_values[i][j]):
            series = prefix[i][j] + '_' + str(k + 1)
            line = data.loc[data['series'] == series].reset_index()
            true_d.append(0.1 * k)
            computed_d.append(line[column].iloc[0])
        plt.plot(np.array([xmin, xmax]), np.array([xmin, xmax]), 'k-')
        plt.plot(np.array(true_d), np.array(computed_d), 'bo', markersize=10, label=prefix[i][j])
        plt.xlim([xmin, xmax])
        plt.ylim([ymin, ymax])
        plt.xlabel('True value of d', fontsize=24)
        plt.ylabel('Computed value of d', fontsize=24)
        plt.legend(loc=2, fontsize=20, frameon=False)
plt.tight_layout()
plt.savefig('FARIMA_' + method + '.eps', format='eps')
plt.close(1)
