import pandas as pd
import matplotlib.pyplot as plt
import sys
from os.path import expanduser

save_location = expanduser('~') + '/.network_speed_log.csv'

class networkData:
    def __init__(self):
        history = pd.read_csv(save_location, header = None, names = ["time", "ping", "upload", "download" ,"ssid"])
        history.fillna('0', inplace = True)
        networks = history['ssid'].unique()

        data = {}

        for i in networks:
            target = history['ssid'] == i
            current = history.loc[target,:].reset_index()
            data[i] = current

        for i in data.keys():
            data[i].drop('ssid', axis = 1, inplace = True)

        dataNaN = data.copy()

        for i in data.keys():
            data[i]['time'] = pd.to_datetime(data[i]['time'], unit='s').dt.round('5min')
            data[i].drop_duplicates(subset = 'time', inplace = True)
            data[i].reset_index(inplace = True)
            data[i].set_index('time', inplace = True)
            data[i].drop(['level_0', 'index'],axis = 1, inplace = True)
            dataNaN[i] = data[i].resample('5T').asfreq()

        self.data = data
        self.dataNaN = dataNaN
        self.ssids = list(data.keys())

    def plotter(self, ssid, metric):
        if ssid in self.ssids:
            if metric in ['ping', 'download', 'upload']:
                plt.figure()
                title = 'Graph of ' + str(metric) + ' over time for SSID ' + str(ssid)
                plt.title(title)
                plt.xlabel('Time')
                plt.ylabel(metric)
                self.data[ssid][metric].plot()
                plt.savefig('.temp_display.png')

#### Run this only if the file has been run directly

if sys.argv[0] == 'grapher.py':
    data = networkData()
    data.plotter(data.ssids[0])
