# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月29日

@author: bob

What's really happening here is that two different Axes instances are placed such
that one is on top of the other. The data for y1 will go in the first Axes instance, and
the data for y2 will go in the second Axes instance.
The twinx() function does the trick: it creates a second set of axes, putting the new
ax2 axes at the exact same position of ax1, ready to be used for plotting.
The complementary function, twiny(), allows us to share the Y-axis with two
different X-axes.
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.arange(0.0, np.e, 0.01)
    y1 = np.exp(-x)
    y2 = np.log(x)
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y1)
    ax1.set_ylabel('Y values for exp(-x)')
    
    ax2 = ax1.twinx()
    ax2.plot(x, y2)
    ax2.set_xlim([0, np.e])
    ax2.set_ylabel('Y values for ln(x)')
    ax1.set_xlabel('Same X for both exp(-x) and ln(x)')
    
    plt.show()
