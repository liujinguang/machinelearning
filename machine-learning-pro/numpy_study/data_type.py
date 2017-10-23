#/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 21, 2017

@author: hadoop

自定义数据类型是一种异构数据类型，可以当做用来记录电子表格或数据库中一行数据的结
构。作为示例，我们将创建一个存储商店库存信息的数据类型。其中，我们用一个长度为40个字
符的字符串来记录商品名称，用一个32位的整数来记录商品的库存数量，最后用一个32位的单精
度浮点数来记录商品价格。
'''

from numpy import *

if __name__ == '__main__':
    t = dtype([('name', str_, 40), ('numitems', int32), ('price', float32)])
    print t
    
    itemz = array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)
    print itemz