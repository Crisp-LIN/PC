# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# matplotlib画图中中文显示会有问题，需要这两行设置默认字体
plt.title("ASV_CTF", fontsize=15, fontweight='normal', color='r', loc='left')  # 设置图表标题
plt.xlabel('PC1')  # x轴坐标轴标签
plt.ylabel('PC2')  # y轴坐标轴标签
plt.xlim(xmax=50, xmin=-50)  # x轴数值范围
plt.ylim(ymax=50, ymin=-50)  # y轴数值范围

# P0
x1 = [8.567182681

      ]
y1 = [12.33086745

      ]
# H2
x2 = [-3.246699778

      ]
y2 = [25.46236313

      ]
# P2
x4 = [5.102559708

      ]
y4 = [-1.496260657
      ]
# P7
x3 = [5.320482903

      ]
y3 = [-37.79323058

      ]

'''
x = [2.758153764, -8.140961542, 5.382807778]  # 坐标点x值
y = [-3.522302327, 10.303343, -6.78104067]  # 坐标点y值

legend = ['P', 'H']
'''
annotations = ["P0", "H2", "P7"]  # 坐标标签

# x2 = np.random.normal(7.5, 1.2, 300)
# y2 = np.random.normal(7.5, 1.2, 300)
colors1 = '#FF8C00'  # 点的颜色
colors2 = '#808080'  # 点的颜色
area = np.pi * 3 ** 3  # 点的大小

# 画散点图
plt.scatter(x1, y1, s=area, c=colors2, label='P')  # P0
plt.scatter(x2, y2, s=area, c=colors1, label='H')  # H2
# plt.scatter(x4, y4, s=area, c=colors2, label='P')  # P2
plt.scatter(x3, y3, s=area, c=colors2, label='P')  # P7

"""
for i in enumerate(x):
    if i == 1 or i == 3:
        plt.scatter(x[i], y[i], s=area, c=colors2, label=legend[0])  # 画图
    if i == 2:
        plt.scatter(x[i], y[i], s=area, c=colors2, label=legend[1])
"""

for i, label in enumerate(annotations):
    print(i)
    print(label)
    # plt.annotate(label, (x[i], y[i]), xytext=(x[i] + 0.5, y[i] + 0.5),
    # weight='semibold',
    # color='b')
# plt.plot([0, 9.5], [9.5, 0], linewidth='0.5', color='#000000') # 画线
# plt.savefig(r'C:\Users\jichao\Desktop\大论文\12345svm.png', dpi=300)
# plt.legend(["BJ", "SH",'fff']) # 图例

plt.savefig(r'D:\Work\分析项目\wxy\正式结果整理\16S+宏基因组\16S\文章内容保留\ASVCTF.tiff', bbox_inches='tight',
            dpi=500)
plt.show()   # 保存文件，需要时使用，防止测试时覆盖
"""
plt.title
fontsize设置字体大小，默认12，可选参数 [‘xx-small’, ‘x-small’, ‘small’, ‘medium’, ‘large’,‘x-large’, ‘xx-large’]
fontweight设置字体粗细，可选参数 [‘light’, ‘normal’, ‘medium’, ‘semibold’, ‘bold’, ‘heavy’, ‘black’]
fontstyle设置字体类型，可选参数[ ‘normal’ | ‘italic’ | ‘oblique’ ]，italic斜体，oblique倾斜
verticalalignment设置水平对齐方式 ，可选参数 ： ‘center’ , ‘top’ , ‘bottom’ , ‘baseline’
horizontalalignment设置垂直对齐方式，可选参数：left,right,center
rotation(旋转角度)可选参数为:vertical,horizontal 也可以为数字
alpha透明度，参数值0至1之间
backgroundcolor标题背景颜色
bbox给标题增加外框 ，常用参数如下：
boxstyle方框外形
facecolor(简写fc)背景颜色
edgecolor(简写ec)边框线条颜色
edgewidth边框线条大小
"""
