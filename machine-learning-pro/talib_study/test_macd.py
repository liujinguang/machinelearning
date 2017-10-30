#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 30, 2017

@author: hadoop
'''

import tushare as ts
import pandas as pd
import talib
import matplotlib.pyplot as plt

def my_macd(prices, fast_period=12, slow_period=26, signal_period=9):
    ewma12 = pd.ewma(prices, span=fast_period)  
#     print ewma12
    ewma26 = pd.ewma(prices, span=slow_period) 
    diff = ewma12 - ewma26
    dea = pd.ewma(diff, span=signal_period)
    bar = diff - dea
    return diff, dea, bar


if __name__ == '__main__':
    data = ts.get_k_data('399300', start='2017-01-01')
#     print hd['close'].values
#     print hd['close'][-2]
#     diff, dea, bar = my_macd(hd['close'].values)
#     print diff[-1], dea[-1], bar[-1]
#     print data['close']
       
    macd, signal, hist = talib.MACD(data['close'].values)
#     print macd[-1], signal[-1], hist[-1]
    fig = plt.figure(figsize=[18, 5])
     
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xticks(range(0, len(data['date']), 10))
     
    ax.set_xticklabels(data['date'][::10], rotation=45)
    ax.plot(data['date'], macd, label='MACD')
    ax.plot(data['date'],signal, label='DIFF')
    ax.plot(data['date'],hist, label='DIFF')
    ax.legend(loc='upper left')
     
#     mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'],
#                      width=0.5, colorup='r', colordown='green',
#                      alpha=0.6)
    plt.grid()    
    plt.show()    

