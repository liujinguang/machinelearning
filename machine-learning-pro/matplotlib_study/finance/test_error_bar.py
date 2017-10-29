#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月29日

@author: bob
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.arange(0, 4, 0.2)
    y = np.exp(-x)
    e1 = 0.1 * np.abs(np.random.randn(len(y)))
    plt.errorbar(x, y, yerr=e1, fmt='.-')
    plt.show()