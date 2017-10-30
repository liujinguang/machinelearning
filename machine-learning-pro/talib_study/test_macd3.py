#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 30, 2017

@author: hadoop

https://www.joinquant.com/post/24
http://stock.10jqka.com.cn/zhishi/20151009/c584915820.shtml
'''

import tushare as ts
import pandas as pd
import talib
import matplotlib.pyplot as plt

# 指数平滑均线函数，以price计算，可以选择收盘、开盘价等价格，N为时间周期，m用于计算平滑系数a=m/(N+1)，EXPMA1为前一日值
def f_expma(N, m, EXPMA1, price):
    a = m / (N + 1.0)
    EXPMA2 = a * price + (1 - a) * EXPMA1
    return EXPMA2  # 2为后一天值

def my_macd(prices, fast_period=12, slow_period=26, signal_period=9):
    ewma12 = pd.ewma(prices, span=fast_period)  
    ewma26 = pd.ewma(prices, span=slow_period) 

    diff = ewma12 - ewma26
    dea = pd.ewma(diff, span=signal_period)
    
    
    ewma12_2 = f_expma(fast_period, 2, ewma12, prices)
    ewma26_2 = f_expma(slow_period, 2, ewma26, prices)
    
    diff_2 = ewma12_2 = ewma26_2    

    bar = diff - dea
    return diff, dea, bar

def macd(prices, fast=12, slow=26, signal=9, m=2.0):
    expma12_1 = pd.ewma(prices, span=fast)  
    expma26_1 = pd.ewma(prices, span=slow) 

    dea = pd.ewma(expma12_1 - expma26_1, span=signal)    

    expma12_2 = f_expma(fast, m, expma12_1, prices)
    expma26_2 = f_expma(slow, m, expma26_1, prices)
    diff2 = expma12_2 - expma26_2
    
#     a = m / (signal + 1)
#     dea2 = a * diff2 + (1 - a) * dea
#     bar2 = 2 * (diff2 - dea2)

    ################
    dea2 = pd.ewma(diff2, span=signal)
    bar2 = 2 * (diff2 - dea2)
#     return EXPMA12_2,EXPMA26?_2,DIFf2,DEA2,BAR2
    return diff2, dea2, bar2

if __name__ == '__main__':
    data = ts.get_k_data('399300', start='2015-01-01')
    print data
#     print hd['close'].values
#     print hd['close'][-2]
#     diff, dea, bar = my_macd(hd['close'].values)
#     print diff[-1], dea[-1], bar[-1]
#     print data['close']
       
#     macd, signal, hist = talib.MACD(data['close'].values)
    diff, dea, macd = macd(data['close'].values)
    print macd[-5], diff[-5], dea[-5]
#     print macd[-1], signal[-1], hist[-1]
    fig = plt.figure(figsize=[18, 5])
      
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xticks(range(0, len(data['date']), 10))
       
    ax.set_xticklabels(data['date'][::10], rotation=45)
#     ax.plot(data['date'], macd, label='MACD', color="red")
    
    ax.plot(data['date'], diff, label='DIFF')
    ax.plot(data['date'], dea, label='DEA')
    ax.legend(loc='upper left')
    
#     ax2 = fig.add_subplot(2,1,2, sharex=ax)
#     ax.bar(data['date'], macd > 0, color='red')
#     ax.bar(data['date'], macd < 0, color='green')
    ax.bar(data['date'], macd, width=0.4, ecolor=['red', 'green'], color='red')
#     ax2.set_xticks(range(0, len(data['date']), 10))
#       
#     ax2.set_xticklabels(data['date'][::10], rotation=45)    
     
    print macd[-1], diff[-1], dea[-1]
    print macd[-5], diff[-5], dea[-5]
      
#     mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'],
#                      width=0.5, colorup='r', colordown='green',
#                      alpha=0.6)
    plt.grid()    
    plt.show()    

