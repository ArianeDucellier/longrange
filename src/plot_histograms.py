"""
This script plots the values of the fractional parameter d
for all the LFE families of a given catalog
"""
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

catalog = 'Sweet_2014'
methods = ['Absolute value', 'Variance', 'Variance of residuals', 'R/S', 'Periodogram']
columns = ['H_absval', 'd_var', 'd_varres', 'd_RS', 'd_p']

Hboxes = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
dboxes = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]

params = {'legend.fontsize': 24, \
          'xtick.labelsize':24, \
          'ytick.labelsize':24}
pylab.rcParams.update(params)
plt.figure(1, figsize=(30, 10))

data = pickle.load(open(catalog + '.pkl', 'rb'))

for i in range(0, len(methods)):
    ax = plt.subplot2grid((1, 5), (0, i))
    if i == 0:
        boxes = Hboxes
    else:
        boxes = dboxes
    plt.hist(data[columns[i]], bins=boxes)
    if i == 0:
        plt.xlabel('Hurst parameter', fontsize=24)
    else:
        plt.xlabel('Fractional index', fontsize=24)
    plt.ylabel('Number of families', fontsize=24)
    plt.title(methods[i], fontsize=24)
plt.tight_layout()
plt.savefig(catalog + '.eps', format='eps')
plt.close(1)
