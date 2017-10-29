#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月28日

@author: bob
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.arange(1, 5)
    plt.plot(x, x * 1.5, label="Normal")
    plt.plot(x, x * 3.0, label="Fast")
    plt.plot(x, x / 3.0, label="Slow")
    plt.grid(True)
    plt.title("Simple Growth of a Measure")
    plt.xlabel("Samples")
    plt.ylabel("Values Measured")
    plt.legend()
    plt.savefig("sample.png")
    plt.show()