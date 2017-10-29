#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月28日

@author: bob

plot() supports an optional third argument that contains a format string for each
pair of X, Y arguments in the form of:
plt.plot(X, Y, '<format>', ...)
There are three levels of customization:
• Colors
• Line styles
• Marker styles

Color abbreviation | Color Name
b blue
c cyan
g green
k black
m magenta
r red
w white
y yellow

There are several ways to specify colors, other than by color abbreviations:
• The full color name, such as yellow, as specified in the Color name column
of the previous table
• Hexadecimal string (the same format as in HTML code) such as #FF00FF
• RGB or RGBA tuples, for example, (1, 0, 1, 1)
• Grayscale intensity, in string format such as '0.7'
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    y = np.arange(1, 3)
    plt.plot(y, 'y', y+1, 'm', y+2, 'c')
    plt.show()