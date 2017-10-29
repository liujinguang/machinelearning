#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月28日

@author: bob
Format strings are really useful, but they have some drawbacks. For example, they
don't allow us to specify different colors for lines and markers

plot() is a really rich function, and there are some keyword arguments to configure
colors, markers, and line styles:
Keyword argument Description
color or c Sets the color of the line; accepts any Matplotlib color format.
linestyle Sets the line style; accepts the line styles seen previously.
linewidth Sets the line width; accepts a float value in points.
marker Sets the line marker style.
markeredgecolor Sets the marker edge color; accepts any Matplotlib color
format.
markeredgewidth Sets the marker edge width; accepts float value in points.
markerfacecolor Sets the marker face color; accepts any Matplotlib color format.
markersize Sets the marker size in points; accepts float values.
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    y = np.arange(1, 3, 0.3)
    plt.plot(y, color='blue', linestyle='dashdot', linewidth=4, marker='o',
             markerfacecolor='red', markeredgecolor='black',
             markeredgewidth=3, markersize=12)
    
    plt.show()