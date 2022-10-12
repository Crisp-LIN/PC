import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

"""
数据处理部分
"""

cazy = pd.read_excel(r'D:\Work\分析项目\wxy\正式结果整理\16S+宏基因组\MAG\lefse\CAZYMES\ND7XG7\lefse_log2FC.xlsx',
                     header=0, index_col=0)
kegg = pd.read_excel(r'D:\Work\分析项目\wxy\正式结果整理\16S+宏基因组\MAG\lefse\KEGG\ND7XG7\lefse_log2FC.xlsx',
                     header=0, index_col=0)
ASV = pd.read_excel(r'D:\Work\分析项目\wxy\宏基因组与16S丰度计算\ASV丰度(加测数据)\ASV_relative_求和去重log2FC_lefse.xlsx',
                    header=0, index_col=0)

cazyfc = pd.DataFrame(cazy, columns=["ND7/ND0", "XG7/ND0", "XG7/ND7"])

"""         画图          """

plt.figure(dpi=600)

# 调整图的大小
plt.figure(figsize=(10, 20))  # 宽 高
# 调整全局字体
plt.rc('font', family='Times New Roman')
plt.title("Plot", fontsize=30, loc='left')  # 标题，并设定字号大小、位置
plt.xticks(size=15)
plt.yticks(size=15)

fig = sns.heatmap(cazyfc, annot=False,
                  # standard_scale：int or None, optional，是否 Min-Max 标准化行 (0) 或列 (1)。
                  xticklabels=True, yticklabels=True, square=False,
                  # (left, bottom, width, height)
                  cmap="RdBu_r",
                  cbar_kws={'label': ' color bar',  # color bar的名称
                            'orientation': 'vertical',  # color bar的方向设置，默认为'vertical'，可水平显示'horizontal'
                            # "ticks":np.arange(4.5, 8, 0.5),  # color bar中刻度值范围和间隔
                            "format": "%.1f",  # 格式化输出color bar中刻度值
                            "pad": 0.1,  # color bar与热图之间距离，距离变大热图会被压缩)  # annot是否显示数值  square 绘图区是否是正方形, cbar设置标尺
                            "shrink": 0.4
                            })
# 调整坐标轴字体
# fig.set_xlabel("X-Axis", fontsize=15)
# fig.set_ylabel("Y-Axis", fontsize=15)
# 调整colorbar的大小和位置
cbar = fig.collections[0].colorbar
cbar.ax.tick_params(labelsize=10)

plt.show()
