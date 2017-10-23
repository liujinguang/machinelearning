#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 22, 2017

@author: hadoop
'''

import numpy as np

if __name__ == '__main__':
    i2 = np.eye(2)
    print i2
    np.savetxt("eye.txt", i2)