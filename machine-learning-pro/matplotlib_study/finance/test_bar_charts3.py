# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月29日

@author: bob
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    data1 = 10 * np.random.rand(5)
    data2 = 10 * np.random.rand(5)
    data3 = 10 * np.random.rand(5)
    
    e2 = 0.5 * np.abs(np.random.randn(len(data2)))
    locs = np.arange(1, len(data1) + 1)
    width = 0.27
    plt.bar(locs, data1, width=width)
    plt.bar(locs + width, data2, yerr=e2, width=width)
    plt.bar(locs + 2 * width, data3, width=width)
    
    plt.xticks(locs + width, locs)
    plt.show()