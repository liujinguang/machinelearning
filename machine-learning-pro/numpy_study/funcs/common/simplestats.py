#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 22, 2017

@author: hadoop
'''

import numpy as np

if __name__ == '__main__':
    c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
    print 'median = ', np.median(c)
    
    sorted = np.msort(c)
    print 'sorted = ', sorted
    
    N = len(c)
    print 'middle = ', sorted[(N - 1) / 2]
    print 'average middle = ', (sorted[N / 2] + sorted[(N - 1) / 2]) / 2
    
    print 'variance = ', np.var(c)
    print 'variance from definition = ', np.mean((c-c.mean())**2)
