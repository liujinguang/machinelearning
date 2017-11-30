# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月17日

@author: bob
'''

from numpy import *

def load_data_set():
    '''
    该函数返回的第一个变量是进行词条切分后的文档集合，这些文档来自斑点狗爱好者留言板
    返回的第二个变量是一个类别标签的集合，这些文本由人工标注，用于训练程序以便自动
    检测侮辱性留言
    '''
    posting_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_vec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    
    return posting_list, class_vec

def create_vocab_list(data_set):
    '''
    创建一个不包含在所有文档中出现的不重复词的列表
    '''
    vocab_set = set([])
    
    # 创建两个集合的并集
    for document in data_set:
        vocab_set = vocab_set | set(document)

    return list(vocab_set)

def set_of_words_2_vec(vocab_lst, input_set):
    '''
    词集模型: set-of-words model
    该函数的输入参数为词汇表及某个文档，输出是文档向量，向量的每个元素为1或0，分别表示
    词汇表中的单词在输入文档中是否出现
    '''
    vec = [0] * len(vocab_lst)
    
    for word in input_set:
        if word in vocab_lst:
            vec[vocab_lst.index(word)] = 1
        else:
            print "the word %s is not in my vocabulary" % word
            
    return vec

def bag_of_words_2_vec(vocab_list, input_set):
    '''
    词袋模型: bags-of-words model
    '''
    vec = [0] * len(vocab_list)
    for word in input_set:
        if word in vocab_list:
            vec[vocab_list.index(word)] += 1
            
    return vec

def train_nb0(train_matrix, train_category):
    '''
    train_matrix: 文档矩阵
    train_category: 每篇文档类别标签所构成的向量
    该处理是一个二类分类的问题，多于多于两类的分类问题，需要对代码稍加修改
    '''
    num_train_docs = len(train_matrix)
    num_words = len(train_matrix[0])
    
    # 计算文档属于侮辱性(abusive)的概率
    pabusive = sum(train_category) / float(num_train_docs)
    
    # 初始化概率, 计算文档属于侮辱性文档(class=1)的概率, 即P(1)，
    p0num = zeros(num_words)
    p1num = zeros(num_words)
    p0Denom = 0.0
    p1Denom = 0.0
    
    # 遍历训练集train_matrix中的所有文档, 一旦某个词语(侮辱性或正常词汇)在某一
    # 文档中出现，则该词对应的个数(p1num或p0num)就加1
    for i in range(num_train_docs):
        if train_category[i] == 1:
            p1num += train_matrix[i]
            p1Denom += sum(train_matrix[i])
        else:
            p0num += train_matrix[i]
            p0Denom += sum(train_matrix[i])
            
    p1vect = p1num / p1Denom
    p0vect = p0num / p0Denom
    
    return p0vect, p1vect, pabusive

def train_nb1(train_matrix, train_category):
    '''
    train_matrix: 文档矩阵
    train_category: 每篇文档类别标签所构成的向量
    该处理是一个二类分类的问题，多于多于两类的分类问题，需要对代码稍加修改
    '''
    num_train_docs = len(train_matrix)
    num_words = len(train_matrix[0])
    
    # 计算文档属于侮辱性(abusive)的概率
    pabusive = sum(train_category) / float(num_train_docs)
    
    # 初始化概率, 计算文档属于侮辱性文档(class=1)的概率, 即P(1)，
    ############################################################
    # 利用贝叶斯分类器对文档进行分类时，要计算多个概率的乘积以获得文档属于某个类别
    # 的概率，如果其中一个概率值为0，那么最后的乘积也为0。为了降低这种影响，可以将
    # 所有词出现数初始化为1， 分母初始化为0
    p0num = ones(num_words)
    p1num = ones(num_words)
    p0Denom = 2.0
    p1Denom = 2.0
    
    # 遍历训练集train_matrix中的所有文档, 一旦某个词语(侮辱性或正常词汇)在某一
    # 文档中出现，则该词对应的个数(p1num或p0num)就加1
    for i in range(num_train_docs):
        if train_category[i] == 1:
            p1num += train_matrix[i]
            p1Denom += sum(train_matrix[i])
        else:
            p0num += train_matrix[i]
            p0Denom += sum(train_matrix[i])
    
    # 为了解决下溢出，采用对数处理
    p1vect = log(p1num / p1Denom)
    p0vect = log(p0num / p0Denom)
    
    return p0vect, p1vect, pabusive
        
def classify_nb(vec2classify, p0vec, p1vec, pclass1):
    '''
    '''
    p1 = sum(vec2classify * p0vec) + log(pclass1)
    p0 = sum(vec2classify * p1vec) + log(1 - pclass1)
    
    if p1 > p0:
        return 1
    else:
        return 0

def testing_nb():
    '''
    '''
    lst_of_posts, lst_of_class = load_data_set()
    vocab_lst = create_vocab_list(lst_of_posts)
#     print vocab_lst
    
    train_matrix = []
    for post_in_doc in lst_of_posts:
        train_matrix.append(set_of_words_2_vec(vocab_lst, post_in_doc))
    
#     print train_matrix
    p0vec, p1vec, pab = train_nb1(array(train_matrix), array(lst_of_class))
    
    test_entry = ['love', 'my', 'dalmation']
    this_doc = array(set_of_words_2_vec(vocab_lst, test_entry))
    res = classify_nb(this_doc, p0vec, p1vec, pab)
    print test_entry, ' classified as: ', res
    
    test_entry = ['love', 'my', 'dalmation']
    this_doc = array(set_of_words_2_vec(vocab_lst, test_entry))
    res = classify_nb(this_doc, p0vec, p1vec, pab)
    print test_entry, ' classified as: ', res    

if __name__ == '__main__':
    testing_nb()
#     lst_of_posts, lst_of_class = load_data_set()
#     vocab_lst = create_vocab_list(lst_of_posts)
# #     print vocab_lst
#     
#     train_matrix = []
#     for post_in_doc in lst_of_posts:
#         train_matrix.append(set_of_words_2_vec(vocab_lst, post_in_doc))
#     
#     print train_matrix
#     p0v, p1v, pab = train_nb0(train_matrix, lst_of_class)
#     print p0v
#     print p1v
#     print pab
    
