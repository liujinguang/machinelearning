#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月28日

@author: bob
'''

import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = range(1, 5)
    plt.plot(x, [xi * 1.5 for xi in x], x, [xi * 3.0 for xi in x])
    plt.show()