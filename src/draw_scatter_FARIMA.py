"""
This script compare the values of the fractional parameter d
computed with the 5 methods for all the synthetic FARIMA time series
"""
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

prefix = ['series_1', 'series_2', 'series_3', 'series_4', 'series_5', 'series_6', \
          'series_7a', 'series_7b', 'series_8a', 'series_8b', 'series_9', 'series_10']

methods = ['Absolute value', 'Variance', 'Variance of residuals', 'R/S', 'Periodogram']
columns = ['H_absval', 'd_var', 'd_varres', 'd_RS', 'd_p']

Hboxes = [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
dboxes = [-0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

true_alpha = np.array([2.0, 2.0, 2.0, 2.0, 2.0, 2.0, \
                       1.5, 1.2, 1.5, 1.2, 1.5, 1.5])

data = pickle.load(open('FARIMA.pkl', 'rb'))[0]

params = {'legend.fontsize': 24, \
          'xtick.labelsize':24, \
          'ytick.labelsize':24}
pylab.rcParams.update(params)

# Loop on series
for i in range(0, len(prefix)):

    data['index_series'] = list(map(lambda x: x.startswith(prefix[i] + '_'), data['series']))
    subdata = data.loc[data['index_series'] == True]

    plt.figure(1, figsize=(25, 25))

    # Loop on methods
    for j in range(0, len(methods)):
        for k in range(0, len(methods)):
            ax = plt.subplot2grid((len(methods), len(methods)), (j, k))

            if j == k:
                if j == 0:
                    plt.hist(subdata[columns[j]], bins = Hboxes)
                else:
                    plt.hist(subdata[columns[j]], bins = dboxes)
            else:
                if j == 0:
                    plt.plot([min(Hboxes) - 1.0 / true_alpha[i], max(Hboxes) - 1.0 / true_alpha[i]], \
                             [min(Hboxes), max(Hboxes)], 'k-')
                else:
                    if k == 0:
                        plt.plot([min(dboxes) + 1.0 / true_alpha[i], max(dboxes) + 1.0 / true_alpha[i]], \
                                 [min(dboxes), max(dboxes)], 'k-')
                    else:
                        plt.plot([min(dboxes), max(dboxes)], [min(dboxes), max(dboxes)], 'k-')
                plt.plot(subdata[columns[k]], subdata[columns[j]], 'bo', markersize=10)
                if j == 0:
                    plt.ylim([min(Hboxes), max(Hboxes)])
                else:
                    plt.ylim([min(dboxes), max(dboxes)])
                if k == 0:
                    plt.xlim([min(Hboxes), max(Hboxes)])
                else:
                    plt.xlim([min(dboxes), max(dboxes)])
            if j == len(methods) - 1:
                plt.xlabel(methods[k], fontsize=24)
            if k == 0:
                plt.ylabel(methods[j], fontsize=24)
    plt.suptitle('FARIMA ' + prefix[i], fontsize=24)
    plt.savefig('scatter_FARIMA/' + prefix[i] + '.eps', format='eps')
    plt.close(1)
      