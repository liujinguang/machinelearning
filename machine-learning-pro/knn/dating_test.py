#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 23, 2017

@author: hadoop
'''

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from array import array
from numpy import shape, zeros, tile
from knn.knn_classifier import do_knn_classifier

def file2matrix(file_name):
    fr = open(file_name)
    array_of_lines = fr.readlines()
    
    # calulate lines of the file
    number_of_lines = len(array_of_lines)
    
    # create zeros matrix
    return_matrix = np.zeros((number_of_lines, 3))
    class_label_vector = []
    
    # parse data from the file lines
    index = 0
    for line in array_of_lines:
        line = line.strip()
        list_from_line = line.split('\t')
        return_matrix[index, :] = list_from_line[0:3]
        class_label_vector.append(int(list_from_line[-1]))
        index += 1
        
#     print return_matrix
#     print class_label_vector
    return return_matrix, class_label_vector

def auto_norm(data_set):
    '''
    normalize the data
    '''
    # 参数0使函数可以从列中选取最小值，而不是当前行的最小值
    min_vals = data_set.min(0)
    max_vals = data_set.max(0)
    ranges = max_vals - min_vals
    norm_data_set = zeros(shape(data_set))
    m = data_set.shape[0]
    
    norm_data_set = data_set - tile(min_vals, (m, 1))
    norm_data_set = norm_data_set / tile(ranges, (m, 1))
    
    return norm_data_set, ranges, min_vals

def dating_class_test():
    '''
    '''
    hold_ratio = 0.1  # hold out ratio
    
    dating_data_mat, dating_labels = file2matrix("datingTestSet2.txt")
    norm_mat, ranges, min_vals = auto_norm(dating_data_mat)
    m = norm_mat.shape[0]
    num_test_vecs = int(m * hold_ratio)
    error_count = 0.0
    
    for i in range(num_test_vecs):
        classifier_result = do_knn_classifier(norm_mat[i, :], norm_mat[num_test_vecs:m, :],
                                              dating_labels[num_test_vecs:m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifier_result, dating_labels[i])
        if (classifier_result != dating_labels[i]): error_count += 1.0
    print "the total error rate is: %f" % (error_count / float(num_test_vecs))
    print error_count

def draw_scatter(dating_date_matrix, dating_labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dating_date_matrix[:, 1], dating_date_matrix[:, 2],
               15.0 * array(dating_labels))
    plt.show()

def classify_person():
    result_lst = ['not at all', 'in small doses', 'in large doess']
    
    percent_tats = float(raw_input("Percentage of time spent playing video games?"))
    ffmiles = float(raw_input("frequent flier miles earned per year?"))
    ice_cream = float(raw_input("Liters of ice cream consumed per year?"))
    
    dating_data_mat, dating_labels = file2matrix("datingTestSet2.txt")
    norm_mat, ranges, min_vals = auto_norm(dating_data_mat)
    in_array = (array([ffmiles, percent_tats, ice_cream]) - min_vals) / ranges
    
    result = do_knn_classifier(in_array, dating_data_mat, dating_labels, 3)
    print "You will probably like this persion: ", result_lst[result-1]

if __name__ == '__main__':
#     mat, label = file2matrix('datingTestSet2.txt')
#     print type(label)
#     draw_scatter(mat, label)
    dating_class_test()
