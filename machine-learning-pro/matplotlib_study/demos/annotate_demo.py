# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月17日

@author: bob
'''

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    ax = plt.subplot(111)
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    plt.plot(t, s, lw=2)
    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.1))
    plt.ylim(-2, 2)
    plt.show()
