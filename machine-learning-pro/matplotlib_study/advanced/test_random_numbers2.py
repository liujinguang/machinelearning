#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月29日

@author: bob
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.arange(0, 10, 0.1)
    y = np.random.randn(len(x))
    plt.plot(x, y)
    plt.title("random numbers")
    plt.show()