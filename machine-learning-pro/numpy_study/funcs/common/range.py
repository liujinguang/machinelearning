#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 22, 2017

@author: hadoop
'''

import numpy as np

if __name__ == '__main__':
    h, l = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5), unpack=True)
    print 'highest = ', np.max(h)
    print 'lowest = ', np.min(l)
    print (np.max(h) + np.min(l)) / 2
    
    print "Spread high price", np.ptp(h)
    print "Spread low price", np.ptp(l)
