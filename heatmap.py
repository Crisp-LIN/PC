import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

"""
数据处理部分
"""
# df = pd.read_table(r'E:\Work\分析项目\wxy\宏基因组与16S丰度计算\cazyme家族丰度\cazy_abundence_sum0311.txt',header=0, index_col=0)
df = pd.read_excel(r'E:\Work\分析项目\wxy\宏基因组与16S丰度计算\KEGG通路与ko号\daixietonglu_abun_meiyouchuliguo_forHeatmap.xlsx',
                   header=0, index_col=0)
row_mean = df.mean(axis=1)  # 求每一行的均值
df.insert(0, 'mean', row_mean)  # 均值的结果作为一列插入df中
df1 = df.sort_values(by='mean', ascending=False)  # 按均值列排序整个表 ascending=False表示降序

df2 = df1.iloc[0:30, 1:16]  # 取df中均值列以外的前30行
df2_cols = list(df2)
for i in df2.columns:
    df2[i + '_log'] = df2[i].map(lambda x: np.log(x))  # 进行对数转换 以 e 为底 想以其他为底可以变换如 np.log10(x)
    dflog = df2.loc[:, df2.columns.str.contains('log')]
dflog.columns = df2_cols  # 换列名

plt.figure(dpi=500)

# sns.clustermap(dflog, cmap='coolwarm')
# 进行数据归一化
# Standardize or Normalize every column in the figure
# Standardize: sns.clustermap(df2, figsize=(5, 5), standard_scale=1)
# sns.clustermap(dflog, figsize=(5, 5), standard_scale=1, cmap="Blues")

fig = sns.clustermap(dflog, figsize=(15, 9),  # 热图 宽 高
                     annot=False, standard_scale=1,  # standard_scale：int or None, optional，是否 Min-Max 标准化行 (0) 或列 (1)。
                     xticklabels=True, yticklabels=True, square=False, cbar_pos=(0.02, 0.8, 0.01, 0.18),
                     # (left, bottom, width, height)
                     cmap="Blues",
                     cbar_kws={'label': ' color bar',  # color bar的名称
                               'orientation': 'vertical',  # color bar的方向设置，默认为'vertical'，可水平显示'horizontal'
                               # "ticks":np.arange(4.5, 8, 0.5),  # color bar中刻度值范围和间隔
                               "format": "%.1f",  # 格式化输出color bar中刻度值
                               "pad": 0.4,  # color bar与热图之间距离，距离变大热图会被压缩)  # annot是否显示数值  square 绘图区是否是正方形, cbar设置标尺
                               })
sns.set(font_scale=0.1)  # 热图及color bar中刻度标签值字号
plt.show()
