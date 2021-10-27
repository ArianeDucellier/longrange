"""
This script looks at the catalog from southern Cascadia (2004-2011) and transform
the LFE detections for each family into a time series
"""

import numpy as np
import pandas as pd
import pickle

from datetime import datetime, timedelta
from math import floor

def get_time_series(filename, threshold, window, tbegin, tend):
    """
    Function to transform the LFE catalog into a time series

    Input:
        type n = string
        n = Name of the LFE template
        type window = float
        window = Duration of the time window where we count the number of LFEs
                 (in seconds)
        type tbegin = obspy UTCDateTime
        tbegin = Beginning time of the catalog 
        type tend = obspy UTCDateTime
        tend = End time of the catalog
    Output:
        type X = numpy array
        X = Time series with number of LFEs per time window
    """

    # Length of the time series
    dt = tend - tbegin
    duration = dt.days * 86400.0 + dt.seconds + dt.microseconds * 0.000001
    nw = int(duration / window)

    # Open LFE catalog
    namedir = 'catalogs/' + filename
    namefile = namedir + '/catalog_2004_2011.pkl'
    df = pickle.load(open(namefile, 'rb'))

    # Filter LFEs
    df = df.loc[df['cc'] * df['nchannel'] >= threshold['threshold_perm'].iloc[i]]

    # Get time series
    X = np.zeros(nw, dtype=int)
    # Loop on LFEs
    for j in range(0, len(df)):
        myYear = df['year'].iloc[j]
        myMonth = df['month'].iloc[j]
        myDay = df['day'].iloc[j]
        myHour = df['hour'].iloc[j]
        myMinute = df['minute'].iloc[j]
        mySecond = int(floor(df['second'].iloc[j]))
        myMicrosecond = int(1000000.0 * (df['second'].iloc[j] - mySecond))
        t = datetime(myYear, myMonth, myDay, myHour, myMinute, mySecond, \
            myMicrosecond)
        # Add LFE to appropriate time window
        if ((tbegin <= t) and (t < tbegin + timedelta(seconds=nw * window))):
            dt = t - tbegin
            duration = dt.days * 86400.0 + dt.seconds + dt.microseconds * \
                0.000001
            index = int(duration / window)
            X[index] = X[index] + 1
    return X

if __name__ == '__main__':

    # List of LFE families
    templates = np.loadtxt('../Plourde_2015/templates_list.txt', \
        dtype={'names': ('name', 'family', 'lat', 'lon', 'depth', 'eH', \
        'eZ', 'nb'), \
             'formats': ('S13', 'S3', np.float, np.float, np.float, \
        np.float, np.float, np.int)}, \
        skiprows=1)

    # Threshold for filtering the catalog
    threshold = pd.read_csv('threshold_cc.txt', sep=r'\s{1,}', header=None, engine='python')
    threshold.columns = ['family', 'threshold_FAME', 'threshold_perm']

    # Beginning and end of the period we are looking at
    tbegin = datetime(2004, 1, 1, 0, 0, 0)
    tend = datetime(2012, 1, 1, 0, 0, 0)

    # We construct the time series by counting the number of LFEs
    # per one-day-long time window
    window = 60.0
    
    # Loop on LFE families
    for i in range(0, np.shape(templates)[0]):
        filename = templates[i][0].astype(str)
        X = get_time_series(filename, threshold, window, tbegin, tend)
        output = 'timeseries/{}.pkl'.format(filename)
        pickle.dump([window, tbegin, tend, X], open(output, 'wb'))


