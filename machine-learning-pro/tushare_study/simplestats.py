#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月14日

@author: bob
'''

import tushare as ts
from pandas import Series, DataFrame
from numpy import *

if __name__ == '__main__':
#     stock = dtype([('date', str_, 10), ('open', float32), ('close', float32), 
#                    ('high', float32), ('low', float32), ('volume', float32), 
#                    ('code', float32)])
#     data = array([("2017-10-18",  11.53,  11.69,  11.70,  11.51,   871365.0,  "000001"),
#                   ("2017-10-19",  11.64,  11.63,  11.72,  11.57,   722764.0,  "000001"),
#                   ("2017-10-20",  11.59,  11.48,  11.59,  11.41,   461808.0,  "000001"),
#                   ("2017-10-23",  11.39,  11.19,  11.40,  11.15,  1074465.0,  "000001")], 
#                  dtype=stock)
#     print type(data)
#     print data
#     itemz = array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)

#     data = [
#             ["2017-10-18",  11.53,  11.69,  11.70,  11.51,   871365.0,  000001],
#             ["2017-10-19",  11.64,  11.63,  11.72,  11.57,   722764.0,  000001],
#             ["2017-10-20",  11.59,  11.48,  11.59,  11.41,   461808.0,  000001],
#             ["2017-10-23",  11.39,  11.19,  11.40,  11.15,  1074465.0,  000001]]
     
#     data_a = np.array(data)
#     print data_a
#     series = Series(data, index=['a', 'b', 'c', 'd'])
#     print series
#     #将Series转换为ndarray类型
#     arr = series.as_matrix()
#     print arr
    
#     arr = Series.as_matrix(self, columns)
#     

    data = [
            [11.53,  11.69,  11.70,  11.51,   871365.0,  000001],
            [11.64,  11.63,  11.72,  11.57,   722764.0,  000001],
            [11.59,  11.48,  11.59,  11.41,   461808.0,  000001],
            [11.39,  11.19,  11.40,  11.15,  1074465.0,  000001]]
    df = DataFrame(data, index=["2017-10-18", "2017-10-19", "2017-10-20", "2017-10-23"], 
                   columns=["open", "close", "high", "low", "volume", "code"])
    
    print "display df"
    print df
    print df.as_matrix(['open', 'close'])
    print df.values
    print array(df)
    
#, index=["date", "open", "close", "high", "low", "volume", "code"]
#     data = ts.get_k_data("000001")
#     aa = data[-20:]
#     print aa
#     print aa.shape