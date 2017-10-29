# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月28日

@author: bob
Markers are, by default, drawn as point markers. They are just a location on the
figure where segments join.
Matplotlib provides a lot of customization options for markers. The following
table contains a list of the available styles:
Marker abbreviation Marker style
. Point marker
, Pixel marker
o Circle marker
v Triangle down marker
^ Triangle up marker
< Triangle left marker
> Triangle right marker
1 Tripod down marker
2 Tripod up marker
3 Tripod left marker
4 Tripod right marker
s Square marker
p Pentagon marker
* Star marker
h Hexagon marker
H Rotated hexagon marker
+ Plus marker
x Cross (x) marker
D Diamond marker
d Thin diamond marker
| Vertical line (vline symbol) marker
_ Horizontal line (hline symbol) marker
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    y = np.arange(1, 3, 0.2)
    plt.plot(y, 'x--', y + 0.5, 'o-.', y + 1, 'D:')
    plt.show()
