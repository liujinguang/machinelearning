#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月10日

@author: bob
'''

import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from numpy.core.defchararray import index

def test_dataframe():
    '''
    '''
    df = pd.DataFrame()
    
    index = ['alpha', 'beta', 'gamma', 'delta', 'eta']
    for i in xrange(5):
        a = DataFrame([np.linspace(i, 5*i, 5)], index=[index[i]])
        df = pd.concat([df, a], axis=0)
        
#     print type(df[1])
    
#     print df
#     print df.iloc[0]
#     print df.loc['alpha']

    #选取行还可以使用切片的方式或者是布尔类型的向量
#     print "Selecting by slices:"
#     print df[1:3]
#     bool_vec = [True, False, True, True, False]
#     print "Selecting by boolean vector:"
#     print df[bool_vec]
    #如果不是需要访问特定行列，而只是某个特殊位置的元素的
    #话， dataframe.at 和 dataframe.iat 是最快的方式，它们分别用于使用索引
    #和下标进行访问：
    print df.iat[2,3]
    print df.at['beta', 0]    
    
    #只要是能转换成 Series 的对象，都可以用于创建 DataFrame
    
    df2 = pd.DataFrame({'A':1, 'B':pd.Timestamp('20171111'), 
                        'C': pd.Series(1.6, index=list(range(4))),
                        'D': np.array([4]*4)})
    print df2
    
def test_date_range():
    '''
    '''
    dates = pd.date_range('20170701', periods=5)
#     print type(dates)
#     
#     print dates
    df = DataFrame(np.random.randn(5,4), index=dates, columns=list('ABCD'))
    print df

if __name__ == '__main__':
    test_dataframe()
    
#     test_date_range()
    
