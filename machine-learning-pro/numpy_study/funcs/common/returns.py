#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 23, 2017

@author: hadoop
'''

import numpy as np

if __name__ == '__main__':
    c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
#     print c
    # NumPy中的diff函数可以返回一个由相邻数组元素的差值构成的数组。
    # 为了计算收益率，我们还需要用差值除以前一天的价格
    returns = np.diff(c) / c[:-1]
    print "Standard deviation = ", np.std(returns)
    
    logreturns = np.diff(np.log(c))
    
    # where函数可以根据指定的条件返回所有满足条件的数组元素的索引值。
    posretindices = np.where(returns > 0)
    print "Indices with positive returns ", posretindices
    
    # 在投资学中，波动率（volatility）是对价格变动的一种度量。历史波动率可以根据历史价
    # 格数据计算得出。计算历史波动率（如年波动率或月波动率）时，需要用到对数收益率。年波动
    # 率等于对数收益率的标准差除以其均值，再除以交易日倒数的平方根，通常交易日取252天。
    annual_volatility = np.std(logreturns) / np.mean(logreturns)
    annual_volatility = annual_volatility / np.sqrt(1. / 252.)
    print "Monthly volatility", annual_volatility * np.sqrt(1. / 12.)
    
