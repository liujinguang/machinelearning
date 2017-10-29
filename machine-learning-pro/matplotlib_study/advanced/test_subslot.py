# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月29日

@author: bob

add_subplot() takes three parameters:
fig.add_subplot(numrows, numcols, fignum)
where:
• numrows represents the number of rows of subplots to prepare
• numcols represents the number of columns of subplots to prepare
• fignum varies from 1 to numrows*numcols and specifies the current
subplot (the one used now)
Basically, we describe a matrix of numrows*numcols subplots that we want into the
Figure; please note that fignum is 1 at the upper-left corner of the Figure and it's
equal to numrows*numcols at the bottom-right corner. The following table should
provide a visual explanation of this:
numrows=2, numcols=2, fignum=1 numrows=2, numcols=2, fignum=2
numrows=2, numcols=2, fignum=3 numrows=2, numcols=2, fignum=4
'''

import matplotlib.pyplot as plt

if __name__ == '__main__':
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot([1, 2, 3], [1, 2, 3])
    ax2 = fig.add_subplot(212)
    ax2.plot([1, 2, 3], [3, 2, 1])
    plt.show()
