#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月14日

@author: bob
'''

import numpy as np

if __name__ == '__main__':
    vec = np.arange(9, dtype=np.float32)
    #打印出一维数组： [ 0.  1.  2.  3.  4.  5.  6.  7.  8.]
    print vec
    #打印对象类型: <type 'numpy.ndarray'>
    print type(vec)
    #打印维数：(9L,)
    print vec.shape
    #打印数组元素的大小
    print vec.dtype.itemsize
    #访问元素: 2.0
    print vec[2]
    #切片: [ 1.  3.  5.  7.]
    print vec[1:9:2]
    