#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月28日

@author: bob

Matplotlib has a couple of useful functions to modify configuration parameters:
• matplotlib.rcdefaults(): Restores Matplotlib's default configuration
parameters values
• matplotlib.rc(): Sets multiple settings in a single command

Matplotlib has another configuration function, to select the backend to use at
runtime, matplotlib.use():
In [1]: import matplotlib as mpl
In [2]: mpl.use('Agg') # to render to file, or to not use a graphical
display
In [3]: mpl.use('GTKAgg') # to render to a GTK UI window
'''

import matplotlib as mpl

if __name__ == '__main__':
    #matplotlib.rcParams is a handy dictionary, global to the whole matplotlib
    #module, which contains default configuration settings
    print mpl.rcParams
    print '*'  * 80
    print mpl.rcParams['ytick.right']
    
    #Matplotlib has a couple of useful functions to modify configuration parameters:
    