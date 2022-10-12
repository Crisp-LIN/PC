import csv
import os
import pandas as pd
def getfilepath(root):
    filenames_list = os.listdir(root)
    filenamesall = []
    for i in filenames_list:
        filenamesall.append(root+i)
    return filenamesall

# newfile = open('E:\\分析项目\\wxy\\wxy0920seq\\wxy0920seq_result_d.csv', "w")

file = getfilepath(root='E:\\分析项目\\wxy\\wxy0920seq_40个蛋白CBM建树\\')
filename = file[3]
# 找到文件名

with open(filename) as yuanshi: # 打开序列ID文件
    reader = csv.reader(yuanshi)
    yuanshi_list = [i for i in reader]
print(filename)

IDindex = {}
print(yuanshi_list)

yuanshi_list_2 = []
for i in range(len(yuanshi_list)):
    pass
    yuanshi_list[i][3] = yuanshi_list[i][3] +'_'+str(i)


datasave = pd.DataFrame(yuanshi_list)
datasave.to_csv('E:\\分析项目\\wxy\\wxy0920seq_40个蛋白CBM建树\\wxy0920seq_result_d_addnum.csv')