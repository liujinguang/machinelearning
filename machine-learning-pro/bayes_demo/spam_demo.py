#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月22日

@author: bob
'''


import re
import random
import numpy as np
from bayes import create_vocab_list, set_of_words_2_vec, train_nb1, classify_nb
# from numpy import *

def text_parse(big_str):
    '''
    接受一个大字符串并将其解析为字符串列表
    '''
    list_of_tokens = re.split(r"\W*", big_str)
    
    return [tok.lower() for tok in list_of_tokens if len(tok) > 2]

def spam_test():
    '''
    '''
    doc_list = []
    class_list = []
    full_txt = []
    
    # 导入并解析文本文件
    for i in range(1, 26):
        word_list = text_parse(open('email/spam/%d.txt' % i).read())
        doc_list.append(word_list)
        full_txt.extend(word_list)
        class_list.append(1)
        
        word_list = text_parse(open('email/ham/%d.txt' % i).read())
        doc_list.append(word_list)
        full_txt.extend(word_list)
        class_list.append(1)        

    vocab_list = create_vocab_list(doc_list)
    training_set = range(50)
    test_set = []
    
    # 随机构建训练集
    for i in range(10):
        rand_index = int(random.uniform(0, len(training_set)))
        #
        test_set.append(training_set[rand_index])
        del(training_set[rand_index])
        
#     print training_set
    
    train_matrix = []
    train_classes = []
    
    
    for doc_index in training_set:
        train_matrix.append(set_of_words_2_vec(vocab_list, doc_list[doc_index]))
        train_classes.append(class_list[doc_index])
        
    p0v, p1v, pspam = train_nb1(np.array(train_matrix), np.array(train_classes))
    error_count = 0
    
    for doc_index in test_set:
        word_vector = set_of_words_2_vec(vocab_list, doc_list[doc_index])
        if classify_nb(np.array(word_vector), p0v, p1v, pspam) != class_list[doc_index]:
            error_count += 1
            
    print "the error rate is: ", float(error_count) / len(test_set)

if __name__ == '__main__':
    spam_test()
    

