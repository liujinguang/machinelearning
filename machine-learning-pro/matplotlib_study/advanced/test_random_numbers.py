#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月29日

@author: bob

Let's see from the higher levels to the lower ones how objects are nested:
Object Description
FigureCanvas     Container class for the Figure instance
Figure           Container for one or more Axes instances
Axes             The rectangular areas to hold the basic elements, such as lines,
                 text, and so on
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.arange(0, 10, 0.1)
    y = np.random.randn(len(x))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x, y)
    ax.set_title('random numbers')
    plt.show()
    plt.plot(x, y)
    plt.title("random numbers")
    plt.show()