# /usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 20, 2017

@author: hadoop
'''

from numpy import tile, array
import operator

def get_data_set():
    '''
    Get data set and labels
    '''
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    
    return group, labels

def classify(in_x, data_set, labels, k):
    '''
    classify the in_x according the data set and labels
    '''
    
    # calcualte the distances
    data_set_size = data_set.shape[0]
    diff_matrix = tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_matrix = diff_matrix ** 2
    sq_distance = sq_diff_matrix.sum(axis=1)
    distances = sq_distance ** 0.5
    print distances
    sorted_dist_indicies = distances.argsort()
    print sorted_dist_indicies
    
    # choose the shortest distance
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist_indicies[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    print class_count
    
    # sort
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    print sorted_class_count
    
    return sorted_class_count[0][0]

if __name__ == '__main__':
    group, labels = get_data_set()
    t = classify(array([0., 0.1]), group, labels, 3)
    print t
#     print type(group)
#     print labels
