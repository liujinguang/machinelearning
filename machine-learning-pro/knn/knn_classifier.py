#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月16日

@author: bob
'''

from numpy import tile
import operator

def auto_normalize_data(data_set):
    '''
       对数据集进行归一化操作
    '''
    # 参数0使函数可以从列中选取最小值，而不是当前行的最小值
    min_vals = data_set.min(0)
    max_vals = data_set.max(0)
    ranges = max_vals - min_vals
    
    
    # 归一化处理
    m = data_set.shape[0]    
    norm_data_set = data_set - tile(min_vals, (m, 1))
    norm_data_set = norm_data_set / tile(ranges, (m, 1))
    
    return norm_data_set, ranges, min_vals

def do_knn_classifier(in_array, data_set, labels, k):
    '''
    classify the in_array according the data set and labels
    '''
    
    #计算距离适量
    data_set_size = data_set.shape[0]
    diff_matrix = tile(in_array, (data_set_size, 1)) - data_set
    sq_diff_matrix = diff_matrix ** 2
    sq_distance = sq_diff_matrix.sum(axis=1)
    distances = sq_distance ** 0.5
    
    #argsort函数返回的是数组值从小到大的索引值， 距离排序
    sorted_dist_indicies = distances.argsort()
        
    # 选择K个紧邻
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist_indicies[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    
    #排序，并返回最相邻的分类
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    
    return sorted_class_count[0][0]

if __name__ == '__main__':
    pass