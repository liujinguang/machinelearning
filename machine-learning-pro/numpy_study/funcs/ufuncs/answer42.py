#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 23, 2017

@author: hadoop
'''

import numpy as np

def ultimate_answer(a):
    result = np.zeros_like(a)
    result.flat = 42
    
    return result

if __name__ == '__main__':
    ufunc = np.frompyfunc(ultimate_answer, 1, 1)
    print "The answer ", ufunc(np.arange(4))
    print "The answer", ufunc(np.arange(4).reshape(2, 2))