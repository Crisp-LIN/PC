import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def heatmap_mean_order(filetype, datapath, row_start=0, row_end=30, col_start=1, col_end=16,
                       figsizel=5, figsizer=5, cmap="Blues"):
    if filetype == 'excel':
        df = pd.read_excel(datapath, header=0, index_col=0)
    elif filetype == 'txt':
        df = pd.read_table(datapath, header=0, index_col=0)

    row_mean = df.mean(axis=1)  # 求每一行的均值
    df.insert(0, 'mean', row_mean)  # 均值的结果作为一列插入df中
    df1 = df.sort_values(by='mean', ascending=False)  # 按均值列排序整个表 ascending=False表示降序
    df2 = df1.iloc[row_start:row_end, col_start:col_end]  # 取df中均值列以外的前x行
    df2_cols = list(df2)

    for i in df2.columns:
        df2[i+'_log'] = df2[i].map(lambda x: np.log(x))  # 进行对数转换 以 e 为底 想以其他为底可以变换如 np.log10(x)
        df_log = df2.loc[:, df2.columns.str.contains('log')]
    df_log.columns = df2_cols

    sns.clustermap(df_log, figsize=(figsizel, figsizer), standard_scale=1, cmap=cmap)
    return plt.show()


heatmap_mean_order(filetype='excel',
                   datapath=r'E:\Work\分析项目\wxy\宏基因组与16S丰度计算\KEGG通路与ko号\daixietonglu_abun_meiyouchuliguo.xlsx',
                   figsizel=10, figsizer=5)


