#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月15日

@author: bob
'''

import tushare as ts
import numpy as np

def 

if __name__ == '__main__':
    stock_id = "000001"
    data = ts.get_k_data(stock_id)
    print data[-10:]
    arr = data[-10:].as_matrix(['close']).flatten()
    print arr
    returns = np.diff(arr)/arr[:-1]
    print returns
    