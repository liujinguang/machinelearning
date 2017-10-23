#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 22, 2017

@author: hadoop

'''

import numpy as np

if __name__ == '__main__':
    c,v = np.loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)
    
    #VWAP（Volume-Weighted Average Price，成交量加权平均价格）是一个非常重要的经济学量，
    #它代表着金融资产的“平均”价格。某个价格的成交量越高，该价格所占的权重就越大。VWAP
    #就是以成交量为权重计算出来的加权平均值，常用于算法交易。
    vwap = np.average(c, weights=v)
    
    print vwap 
    print np.mean(c)
    
    #在经济学中，TWAP（Time-Weighted Average Price，时间加权平均价格）是另一种“平均”
    #价格的指标。其实TWAP只是一个变种而已，基本的思想就是最近的价格重要性大一些，
    #所以我们应该对近期的价格给以较高的权重。
    t = np.arange(len(c))
    print 'twap = ', np.average(c, weights=t)