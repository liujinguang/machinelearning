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

if __name__ == '__main__':
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
#     plt.grid()    
#     plt.show()
