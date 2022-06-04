import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np

nt = 10
t = np.arange(-nt, nt + 1, 1)

poisson = np.zeros(2 * nt + 1)
poisson[nt] = 1

phi = 0.5
AR = np.zeros(2 * nt + 1)
for i in range(0, len(t)):
    AR[i] = phi ** abs(t[i])

delta = 0.5
LRD = np.zeros(2 * nt + 1)
for i in range(0, len(t)):
    LRD[i] = abs(t[i]) ** (- delta)

params = {'legend.fontsize': 24, \
          'xtick.labelsize':24, \
          'ytick.labelsize':24}
pylab.rcParams.update(params)

plt.figure(1, figsize=(15, 5))
plt.plot(t, LRD, 'go', label='LRD', markersize=8)
plt.plot(t, AR, 'bo', label='AR(1)', markersize=8)
plt.plot(t, poisson, 'ro', label='Poisson', markersize=8)
plt.xlabel('Units of time', fontsize=24)
plt.ylabel('Autocorrelation', fontsize=24)
plt.title('Correlation between number of LFEs per unit of time', fontsize=24)
plt.legend(loc=1, fontsize=24)
plt.tight_layout()
plt.savefig('ACFs.eps', format='eps')
plt.close(1)
