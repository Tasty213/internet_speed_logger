import pandas as pd
import matplotlib.pyplot as plt


class networkData:
    def __init__(self):
        print('working')
        history = pd.read_csv('output.csv')
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
        
        del data['0']
        del dataNaN['0']
        
        self.data = data
        self.dataNaN = dataNaN
        self.ssids = list(data.keys())

    def plotter(self, ssid):
        if ssid in self.ssids:
            for i in self.data[ssid].columns:
                plt.figure()
                title = 'Graph of ' + str(i) + ' over time for SSID ' + str(ssid)
                plt.title(title)
                plt.xlabel('Time')
                plt.ylabel(i)
                self.data[ssid][i].plot()
                plt.show()
                print(title)
