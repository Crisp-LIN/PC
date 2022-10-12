# 散点图：
import matplotlib.pyplot as plt
from pylab import mpl

# 设置中文字体
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 解决图像保存时负号'-'显示为方框的问题
mpl.rcParams['axes.unicode_minus'] = False
grade = ["一年级", '二年级', '三年级', '四年级', '五年级']
gpa = [2.1, 2.3, 2.5, 3.1, 3.5]
# 定义散点图标题
plt.title("各年级平均GPA", fontsize=15, color='r')
# 定义坐标轴
plt.xlabel("年级", fontsize=15, color='r')
plt.ylabel("GPA", fontsize=15, color='r')
index = list(range(len(grade)))  # 找坐标等量的刻度
# 对于x刻度的设置
plt.xticks(index, grade, fontsize=15, rotation=90)
# 绘图展示
plt.scatter(index, gpa, color='r', s=50, marker='>')
plt.show()
# plt.scatter注释：    散点图
# scatter(x, y, color, s, marker)
# x：自变量
# y：因变量
# color：散点的颜色
# s：散点的大小
# 标记(marker)：.(散点) ,(正方形) o(圆) ^(上三角形) <(左三角形) >(右三角形)
# 颜色(color)
