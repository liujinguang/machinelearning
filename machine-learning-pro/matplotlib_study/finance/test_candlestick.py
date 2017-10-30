# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月29日

@author: bob

https://zhuanlan.zhihu.com/p/28584048

'''

import numpy as np
import tushare as ts
import talib
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import pandas as pd

def my_macd(price, fastperiod=12, slowperiod=26, signalperiod=9):
    ewma12 = pd.ewma(price,span=fastperiod)
    ewma60 = pd.ewma(price,span=slowperiod)
    dif = ewma12-ewma60
    dea = pd.ewma(dif,span=signalperiod)
    bar = (dif-dea) #有些地方的bar = (dif-dea)*2，但是talib中MACD的计算是bar = (dif-dea)*1
    return dif[-1],dea[-1],bar[-1]

if __name__ == '__main__':
<<<<<<< HEAD
    data = ts.get_k_data('399300', index=True, start='2017-01-01')
    sma_10 = talib.SMA(np.array(data['close']), 10)
    sma_30 = talib.SMA(np.array(data['close']), 30)
#     print data
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xticks(range(0, len(data['date']), 10))
     
    ax.set_xticklabels(data['date'][::10], rotation=45)
    ax.plot(sma_10, label='10')
    ax.plot(sma_30, label='30')
    ax.legend(loc='upper left')
     
    macd, signal, hist = talib.MACD(data['close'].values, fastperiod=12, slowperiod=26, signalperiod=9)
#     print macd[-1], signal[-1], hist[-1]
    print my_macd(data['close'].values)
#     print (macd[-1] - signal[-1])*2
#     print talib.MACD(np.ndarray(data['close']))
#      
#     mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'],
#                      width=0.5, colorup='r', colordown='green',
#                      alpha=0.6)
#      
=======
    data = ts.get_k_data('399300', index=True, start='2017-10-01')
    print data
#     sma_10 = talib.SMA(np.array(data['close']), 10)
#     sma_30 = talib.SMA(np.array(data['close']), 30)
#     
#     fig = plt.figure()
#     ax = fig.add_subplot(1, 1, 1)
#     ax.set_xticks(range(0, len(data['date']), 10))
#     
#     ax.set_xticklabels(data['date'][::10], rotation=45)
#     ax.plot(sma_10, label='10')
#     ax.plot(sma_30, label='30')
#     ax.legend(loc='upper left')
#     
#     mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'],
#                      width=0.5, colorup='r', colordown='green',
#                      alpha=0.6)
>>>>>>> 85a2daa1a8c77b1b8b9959aae14dd29297d83c94
#     plt.grid()    
#     plt.show()
