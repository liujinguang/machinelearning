#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

A = np.eye(2)
print "A", A
B = 2 * A
print "B", B
print "Compound matrix\n", np.bmat("A B; A B")

