# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月28日

@author: bob
'''

import matplotlib.pyplot as plt

if __name__ == '__main__':
    #This code line is the actual plotting command. We have specified only a 
    #list of values that represent the vertical coordinates of the points to 
    #be plotted
    plt.plot([1, 4, 3, 2, 5])
    plt.show()
    #Matplotlib will use an implicit horizontal values list, from 0 (the first 
    #value) to N-1 (where N is the number of items in the list).
