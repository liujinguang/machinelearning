'''
Created on Oct 21, 2017

@author: hadoop
'''

import numpy as np
from datetime import datetime

def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    return a + b

def pythonsum(n):
    result = []
    for i in xrange(n):
        result.append(i ** 2 + i ** 3)
        
    return result

if __name__ == '__main__':
    
    size = 2000
    start = datetime.now()
    c = pythonsum(size)
    delta = datetime.now() - start
    print "The last 2 elements of the sum", c[-2:]
    print "PythonSum elapsed time in microseconds", delta.microseconds
    start = datetime.now()
    c = numpysum(size)
    delta = datetime.now() - start
    print "The last 2 elements of the sum", c[-2:]
    print "NumPySum elapsed time in microseconds", delta.microseconds    
    start = datetime.now()
