# /usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年11月15日

@author: bob
'''

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.arange(0, 10, 0.2)
    y1 = np.cos(x)
    y2 = np.sin(x)
    y3 = np.sqrt(x)
    
    
    # 坐标轴上移
    ax = plt.subplot(111)
    
    # 去掉边框线：右、上
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    # 移动下边框线，相当于移动x轴
    ax.xaxis.set_ticks_position('bottom') 
    ax.spines['bottom'].set_position(('data', 0))
     
#     #移动左边边框，相当于移动y轴
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    
    # 设置标题、x轴、y轴,  其中，r’……’ 语句表示使用 LaTex 公式符号
    plt.title(r'$the \ function \ figure \ of \ cos(), \ sin() \ and \ sqrt()$', fontsize=19)
    plt.xlabel(r'$the \ input \ value \ of \ x$', fontsize=18, labelpad=88.8)
    plt.ylabel(r'$y = f(x)$', fontsize=18, labelpad=12.5)
    
    # 设置x, y轴的刻度范围
    plt.xlim(x.min() * 1.1, x.max() * 1.1)
    plt.ylim(-1.5, 4.0)
    

    # 设置 x, y 轴的刻度标签值
    plt.xticks([2, 4, 6, 8, 10], [r'2', r'4', r'6', r'8', r'10'])
    plt.yticks([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0],
               [r'-1.0', r'0.0', r'1.0', r'2.0', r'3.0', r'4.0'])    
    
    # 在数据图中添加文字描述 text
    plt.text(4, 1.68, r'$x \in [0.0, \ 10.0]$', color='k', fontsize=15)
    plt.text(4, 1.38, r'$y \in [-1.0, \ 4.0]$', color='k', fontsize=15)

    
    # 绘制 3 条函数曲线
    ax.plot(x, y1, color='blue', linewidth=1.5, linestyle='-', marker='.', label=r'$y = cos{x}$')
    ax.plot(x, y2, color='green', linewidth=1.5, linestyle='-', marker='*', label=r'$y = sin{x}$')
    ax.plot(x, y3, color='m', linewidth=1.5, linestyle='-', marker='x', label=r'$y = \sqrt{x}$')
    
    # 显示中文: 默认的编程环境无法显示中文字符，这里提供一种方法，添加如下配置代码：
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    
    # 设置图例 在 plt.plot 函数中添加 label 参数后，使用 plt.legend(loc=’up right’)
    plt.legend(loc="up right")
    
    plt.show()
    
