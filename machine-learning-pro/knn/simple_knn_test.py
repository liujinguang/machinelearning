#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月16日

@author: bob
'''

from numpy import array
from knn.knn_classifier import do_knn_classifier

def get_data_set():
    '''
    Get data set and labels
    '''
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    
    return group, labels

if __name__ == '__main__':
    data_set, labels = get_data_set()
    
    t = do_knn_classifier(array([0.2, 0.1]), data_set, labels, 3)
    print t