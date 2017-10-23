#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 23, 2017

@author: hadoop
'''

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

def file2matrix(file_name):
    fr = open(file_name)
    array_of_lines = fr.readlines()
    
    #calulate lines of the file
    number_of_lines = len(array_of_lines)
    print number_of_lines
    
    #create matrix
    return_matrix = np.zeros((number_of_lines, 3))
    class_label_vector = []
    
    #parse data from the file lines
    index = 0
    for line in array_of_lines:
        line = line.strip()
        list_from_line = line.split('\t')
        return_matrix[index, :] = list_from_line[0:3]
        class_label_vector.append(int(list_from_line[-1]))
        index += 1
        
    print return_matrix
    print class_label_vector
    return return_matrix, class_label_vector
        
def draw_scatter(dating_date_matrix):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dating_date_matrix[:, 1], dating_date_matrix[:,2])
    plt.show()

if __name__ == '__main__':
    mat, label = file2matrix('datingTestSet2.txt')
    draw_scatter(mat)