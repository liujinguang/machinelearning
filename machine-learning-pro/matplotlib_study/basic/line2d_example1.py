#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月28日

@author: bob
'''

import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = range(10)
    plt.plot(x, [xi ** 2 for xi in x])
    plt.show()