#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月8日

@author: bob
'''

import numpy as np
from pandas import Series, DataFrame

if __name__ == '__main__':
    s = Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'], name='test')
    print s.index
