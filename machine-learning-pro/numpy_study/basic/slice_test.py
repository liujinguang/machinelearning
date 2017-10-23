#/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 21, 2017

@author: hadoop
'''
from numpy import arange

if __name__ == '__main__':
#     a = arange(10)
#     print a         #[0 1 2 3 4 5 6 7 8 9]
#     
#     print a[3:7]    #[3 4 5 6]
#     print a[::2]    #[0 2 4 6 8]
#     print a[::-1]   #[9 8 7 6 5 4 3 2 1 0]
#     
#     print "*" * 80
    #reshape函数的作用是改变数组的“形状”，也就是改变数组的维度，其参数为一个正整数元组，
    #分别指定数组在每个维度上的大小。
    b = arange(24).reshape(2,3,4)
    print b
    
    print b[:, 0, 0]
    print b[0, :, :]
    print b[0, ...]