# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月16日

@author: bob
'''

from math import log
import operator
import pickle
from decision_tree.tree_plotter import retrieve_tree

# pylint: disable=redefined-outer-name

def calculate_shannon_entropy(data_set):
    '''
       计算香农熵
    '''
    # 计算数据集中实例的总数
    num_entries = len(data_set)
    label_counts = {}

    # 为所有可能分类创建字典
    for vec in data_set:
        # 键值为最后一列的数值
        current_label = vec[-1]
        if current_label not in label_counts.keys():
            label_counts[current_label] = 0
            
        label_counts[current_label] += 1
        
    # 计算熵值
    shannon_entropy = 0 
    for key in label_counts:
        # 适用类标签发生的频率计算类别出现的概率
        prob = float(label_counts[key]) / num_entries
        
        # 计算香农熵
        shannon_entropy -= prob * log(prob, 2)
    
    return shannon_entropy

def create_data_set():
    '''
        创建数据集
    '''
    data_set = [[1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    
    return data_set, labels    

def split_data_set(data_set, axis, value):
    '''
        划分数据集
    '''
    ret_data_set = []
    
    for vec in data_set:
        if vec[axis] == value:  # 将符合特征的数据抽取出来            
            reduced_vec = vec[:axis]
            reduced_vec.extend(vec[axis + 1:])
            ret_data_set.append(reduced_vec)
            
    return ret_data_set

def choose_best_features_to_split(data_set):
    '''
        实现选取特征，划分数据集，计算得出最好的划分数据集的特征
        函数调用需要满足一定的要求：
        1. 数据必须是一种由列表元素组成的列表，而且所有列表都要有相同的数据长度
        2. 数据的最后一列或每个实例的最后一个元素是当前实例的分类标签
    '''
    num_features = len(data_set[0]) - 1
    # 计算整个数据集的原始香农熵
    base_entropy = calculate_shannon_entropy(data_set)
    best_info_gain = 0.0
    best_feature = -1 
    
    for i in range(num_features):  # 遍历所有的特征
        # 将数据集中所有的第i个特征值或所有可能存在的值写入这个新的list
        feat_list = [example[i] for example in data_set]
        unique_vals = set(feat_list)
        
        # 计算每种划分的信息熵
        new_entropy = 0.0
        for value in unique_vals:            
            sub_data_set = split_data_set(data_set, i, value)
            prob = len(sub_data_set) / float(len(data_set))
            new_entropy += prob * calculate_shannon_entropy(sub_data_set)
            
        # 计算最好的信息熵增益。信息增益是熵的减少或者是数据无序度的减少
        info_gain = base_entropy - new_entropy        
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
            
    return best_feature

def majority_count(class_lst):
    '''
        该函数使用分类名称的列表，并返回出现次数最多的分类名称
    '''
    class_count = {}
    
    for vote in class_lst:
        if vote not in class_count.keys():
            class_count[vote] = 0
        class_count[vote] += 1
        
        sorted_class_count = sorted(class_count.iteritems(), 
                                    key=operator.itemgetter(1), reverse=True)
        
        return sorted_class_count[0][0]

def create_tree(data_set, labels):
    '''
    '''
    #收集数据集中所有的类标签
    class_list = [example[-1] for example in data_set]
    
    #类别完全相同，则停止继续分类
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    
    #遍历完所有特征，返回出现次数最多的分类
    if len(data_set[0]) == 1:
        return majority_count(class_list)
    
    best_feat = choose_best_features_to_split(data_set)
    best_feat_label = labels[best_feat]
    
    my_tree = {best_feat_label:{}}  #使用字典类型存储树的信息
    del(labels[best_feat])
    
    #遍历当前选择特征值包含的所有属性值
    feat_values = [example[best_feat] for example in data_set]
    unique_values = set(feat_values)
    for value in unique_values:
        sub_labels = labels[:]
        my_tree[best_feat_label][value] = create_tree(split_data_set(data_set, best_feat, value), sub_labels)

    return my_tree

def do_classifier(in_tree, feat_labels, test_vec):
    '''
    在执行数据分类时，需要决策树以及用于构造树的标签向量。然后，
    比较测试数据与决策树上的数值，递归执行该过程直到进入叶子节点，
    最后将测试数据定义为叶子节点所属的类型
    '''
    first_str = in_tree.keys()[0]
    second_dict = in_tree[first_str]
    feat_index = feat_labels.index(first_str)   #将标签字符串转换为索引
    for key in second_dict.keys():
        if test_vec[feat_index] == key:
            if type(second_dict[key]).__name__ == "dict":
                class_label = do_classifier(second_dict[key], feat_labels, test_vec)
            else:
                class_label = second_dict[key]

    return class_label

def store_tree(in_tree, file_name):
    '''
    存储决策树
    '''
    fw = open(file_name, 'w')
    pickle.dump(in_tree, fw)
    fw.close()

def grab_tree(file_name):
    '''
    '''
    fr = open(file_name)
    res = pickle.load(fr)
    fr.close()
    
    return res

if __name__ == '__main__':
    data_set, labels = create_data_set()
#     print labels
#     print create_tree(data_set, labels)
    print do_classifier(retrieve_tree(0), labels, [1, 0])
