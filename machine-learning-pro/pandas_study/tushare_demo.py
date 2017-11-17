#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月11日

@author: bob
'''

import tushare as ts

if __name__ == '__main__':
    data = ts.get_k_data('000001', start="2017-11-01")
    print type(data)
    print data.shape
#     print "Head of this DataFrame:"
#     print data.head(3)
#     print "Tail of this DataFrame:"
#     print data.tail(5)
    
    #dataframe.describe() 提供了 DataFrame 中纯数值数据的统计信息
#     print data.describe()
    
    #dataframe.describe() 提供了 DataFrame 中纯数值数据的统计信息
#     for i in  data['date']:
#         print i

    #对数据的排序将便利我们观察数据， DataFrame 提供了两种形式的排序。一种是
    #按行列排序，即按照索引（行名）或者列名进行排序，可调
    #用 dataframe.sort_index ，指定 axis=0 表示按索引（行名）排
    #序， axis=1 表示按列名排序，并可指定升序或者降序
    print data
    
#     print data.sort_index(axis=0, ascending=True).head()
    
    #第二种排序是按值排序，可指定列名和排序方式，默认的是升序排序
#     print data.sort_values(by=['volume', 'close'], axis=0, ascending=[True, False])

#     print data.iloc[1:3][:]

    #使用 loc 、 iloc 、 at 、 iat 、 ix 以及 [] 访问 DataFrame 数据的几种方式
    print data.iloc[1:4]
    
    #使用布尔类型的向量获取数据的方法，可以很方便地过滤数据，例如，我们要选出收盘价
    #在均值以上的数据n
#     print data[data.close > data.open]
#     print data[data.date == "2017-11-02"]

    #数据操作
    #Series 和 DataFrame 的类函数提供了一些函数，如 mean() 、 sum() 等，指
    #定0按列进行，指定1按行进行
#     print data.mean(0)
    
    #value_counts 函数可以方便地统计频数
#     print data['low'].value_counts()
    
    #在 panda 中， Series 可以调用 map 函数来对每个元素应用一个函
    #数， DataFrame 可以调用 apply 函数对每一列（行）应用一个函
    #数， applymap 对每个元素应用一个函数。这里面的函数可以是用户自定义的一个
    #lambda函数，也可以是已有的其他函数。下例展示了将收盘价调整到 [0, 1] 区间
    print data[['close']].apply(lambda x: (x - x.min()) / (x.max() - x.min()))