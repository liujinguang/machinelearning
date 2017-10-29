#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月29日

@author: bob

Histogram plots group up values into bins of values. By default, hist() uses a bin
value of 10 (so only ten categories, or bars, are computed), but we can customize
it, either by passing an additional parameter, for example, in hist(y, <bins>), or
using the bin keyword argument as hist(y, bin=<bins>).

'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    y = np.random.randn(10000000)
    plt.hist(y, 1000)
    plt.show()