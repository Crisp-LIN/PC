import numpy as np
import pandas as pd
from pylab import mpl
import matplotlib.pyplot as plt
import seaborn as sns


def retu(df):
    # df = df.set_index('ID')
    df_3 = df.values
    y = df.index.to_list()
    mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置中文字体
    mpl.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(12, 8))  # 画布大小
    fig = sns.heatmap(pd.DataFrame(np.round(df_3, 2),
                                   columns=['3012', '49', 'JSB', '白', '酵母', '球'],
                                   index=y), annot=False, vmax=1, vmin=0,
                      xticklabels=True, yticklabels=True, cbar=False, square=False,
                      cmap="Reds")  # annot是否显示数值  square 绘图区是否是正方形, cbar设置标尺
    cb = fig.figure.colorbar(fig.collections[0])  # 显示color-bar
    cb.ax.tick_params(labelsize=24)
    plt.yticks(fontsize=24, rotation=0, horizontalalignment='right')
    plt.xticks(fontsize=24, rotation=0, horizontalalignment='center')
    scatter_fig = fig.get_figure()
    scatter_fig.savefig('D:\\Desktop\\' + '热图.tif', dpi=500)
    # plt.savefig('C:\\Users\\86184\\Desktop\\'+ day +'热图.tif',dpi = 500) #dpi = 500 调整分辨率
    plt.clf()


x = ['12h', '24h', '36h', '48h', '96h', '144h']
cazy = pd.read_excel(r'D:\Work\分析项目\wxy\正式结果整理\16S+宏基因组\MAG\lefse\CAZYMES\ND7XG7\lefse_log2FC.xlsx',
                   header=0, index_col=0)
cazyfc = pd.DataFrame(cazy, columns=["ND7/ND0","XG7/ND0","XG7/ND7"])
cazyfc.T
retu(cazyfc.T)
"""
for day in x:
    df = pd.read_excel('C:\\Users\\86184\\Desktop\\最新热图\\' + day + '.xlsx')
    retu(df, day)
    """
