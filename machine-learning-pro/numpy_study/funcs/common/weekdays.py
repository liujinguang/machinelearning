#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 23, 2017

@author: hadoop
'''

import numpy as np
from datetime import datetime

def datestr2num(s):
    return datetime.strptime(s, "%d-%m-%Y").date().weekday()

if __name__ == '__main__':
    dates, close = np.loadtxt('data.csv', delimiter=',', converters={1:datestr2num}, usecols=(1, 6),
                              unpack=True)
    
    print dates
    
    averages = np.zeros(5)
    print averages

    # take函数可以按照这些索引值从数组中取出相应的元素。
    for i in range(5):
        indices = np.where(dates == i)
        prices = np.take(close, indices)
        avg = np.mean(prices)
        
        print "Day", i, "prices", prices, "Average", avg
        averages[i] = avg

    # 哪个工作日的平均收盘价是最高的，哪个是最低的
    top = np.max(averages)
    print "Highest average", top
    print "Top day of the week", np.argmax(averages)
    bottom = np.min(averages)
    print "Lowest average", bottom
    print "Bottom day of the week", np.argmin(averages)
    
