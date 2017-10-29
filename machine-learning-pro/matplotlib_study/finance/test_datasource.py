# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年10月29日

@author: bob
'''

from matplotlib.pylab import date2num  
import datetime  
import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
   

   
if __name__ == '__main__':

    # 对tushare获取到的数据转换成candlestick_ohlc()方法可读取的格式  
    data_list = []  
    hist_data = ts.get_hist_data('600199', start="2017-10-01")
    print hist_data
#     exit(0)

    for dates, row in hist_data.iterrows():  
        # 将时间转换为数字  
        date_time = datetime.datetime.strptime(dates, '%Y-%m-%d')  
        t = date2num(date_time)  
        open, high, low, close = row[:4]  
        datas = (t, open, high, low, close)  
        data_list.append(datas)  
        
    print '*' * 80
    print data_list
       
    # 创建子图  
    fig, ax = plt.subplots()  
    fig.subplots_adjust(bottom=0.2)  
    # 设置X轴刻度为日期时间  
    ax.xaxis_date()  
    plt.xticks(rotation=45)  
    plt.yticks()  
    plt.title("ID:600199")  
    plt.xlabel("Time")  
    plt.ylabel("Price(RMB)")  
    mpf.candlestick_ohlc(ax, data_list, colorup='r', colordown='green') #width=1.5,  
    plt.grid()  
    plt.show()
