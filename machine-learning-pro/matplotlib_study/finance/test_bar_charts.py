# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月29日

@author: bob
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    dict = {'A': 40, 'B': 70, 'C': 30, 'D': 85}
    for i, key in enumerate(dict):
        plt.bar(i, dict[key])
    
    plt.xticks(np.arange(len(dict)), dict.keys())
    plt.yticks(dict.values())

    plt.show()
