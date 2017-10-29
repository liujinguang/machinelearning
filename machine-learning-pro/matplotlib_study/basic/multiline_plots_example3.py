# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月28日

@author: bob

The multiline plot is possible because, by default, the hold property is enabled
(consider it as a declaration to preserve all the plotted lines on the current figure
instead of replacing them at every plot() call). Try this simple example and see
what happens:
'''

from time import sleep

import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    x = np.arange(1, 5)
    # enable interactive mode, in case it was not
    plt.interactive(True)
    # empty window will pop up
#     plt.hold(False)
    plt.plot(x, x * 1.5)
    
#     sleep(3)
    plt.plot(x, x * 3.0)
    plt.show()
