# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月28日

@author: bob

All the available styles are listed in the following table:
Style abbreviation     Style
-                      solid line
--                     dashed line
-.                     dash-dot line
:                      dotted line
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    y = np.arange(1, 3)
    plt.plot(y, '--', y + 1, '-.', y + 2, ':')
    plt.show()
