#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月28日

@author: bob

You might have noticed that Matplotlib automatically sets the limits of the figure
to precisely contain the plotted datasets. However, sometimes we want to set the
axes limits ourself (defining the scale of the chart).

The list of values, that's the whole set of four values of keyword arguments [xmin,
xmax, ymin, ymax], allows us to specify at the same time, the minimum and
maximum limits respectively for the X-axis and the Y-axis. We can use the specific
keyword arguments, for example:
plt.axis(xmin=NNN, ymax=NNN)
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.arange(1, 5)
    plt.plot(x, x * 1.5, x, x * 3.0, x, x / 3.0)
    plt.grid(True)
    plt.axis([0, 5, -1, 13])    
    print plt.ylim()
    print plt.xlim()
    plt.show()