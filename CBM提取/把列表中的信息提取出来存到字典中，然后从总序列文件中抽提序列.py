# 把列表中的信息提取出来存到字典中，然后从总序列文件中抽提序列
# file:待处理的文件路径，输入路径函数返回值; Evalueindex(Ei):Evalue那一列的索引数; Evaluethreshold(Et):设置Evalue的阈值，输入阈值
# Idindex(Ii):ID列的索引数，输入索引数;
# Envfrom:带有序列索引的列（头），输入列索引数; Envto:带有序列索引的列（头），输入列索引数
# file_2:序列fasta文件路径，输入路径函数返回值
# newfp:新文件路径，输入路径

import os
import csv
def dictfromlist(file,Evalueindex,Evaluethreshold,Idindex,Envfrom,Envto,file_2,newfp):
    with open(file) as yuanshi:  # 打开csv文件
        reader = csv.reader(yuanshi)  # 读文件
        yuanshi_list = [i for i in reader]  # 把文件每一行存入列表，其中的每一行都自成一个列表

    IDindexdict = {}  # 新建字典
    for i in yuanshi_list:  # 遍历列表yuanshi_list，就是遍历yuanshi的每一行，也是遍历每个列表。
        if float(i[Evalueindex]) <= Evaluethreshold:
            """
            每一行都是列表，用列表索引拿出Evalueindex值，
            把这个值转化为浮点数，与设置的阈值Evaluethreshold比较，
            筛选Evalueindex值小于阈值Evaluethreshold的行。
            """

            index = i[Idindex]  # 把每一行索引值为IDindex的值赋值给变量index
            IDindexdict[index] = i[Envfrom] + ','+ i[Envto] + ','+ i[Evalueindex]
            """
            把字典的索引设置为每一行的Envfrom、Envto、Evalueindex的值的合并
            """

    print(IDindexdict)  # 把字典IDindexdict打印出来看一眼
# 第四步，从序列文件中抽提序列
    fasta = open(file_2, 'r')  # file_2是序列文件
    seq = {}  # 新建一个新的字典seq，把总序列存入字典seq。
    for i in fasta:
        if i.startswith('>'):  # 如果某一行以'>'开头
            o = i.split(" ", 1)[0]  # 把以'>'开头的行做字符串截取处理，并赋值给新的变量
            newid = o.strip('>')  # 切掉字符串里的'>'，并赋值给变量newid
            index = newid  # 把newid赋值给index
            seq[index] = ''  # 把字典seq的值设置为空
        else:
            seq[index] += i.replace('\n', '')  # 如果某一行
    print(len(seq.keys()))
    shaixuanseq = {}
    for i in IDindexdict.keys():
        for p in seq.keys():
            if i.split("_", 1)[0] == p:
                num1 = int(IDindexdict[i].split(",", 2)[0])
                num2 = int(IDindexdict[i].split(",", 2)[1])
                id = '>' + i
                shaixuanseq[id] = seq[p][num1:num2]
    #print(shaixuanseq.items())
    print(len(IDindexdict.keys()))
    newfile = open(newfp, "w+")
    for k, v in shaixuanseq.items():
        newfile.write(k + '\n' + v + '\n')




# 使用示例如下
def getfpath(root,x):
    filenames_list = os.listdir(root)
    filenamesall = []
    for i in filenames_list:
        filenamesall.append(root+i)
    return filenamesall[x]
filename = getfpath(root='E:/分析项目/myself/函数测试文件/',x = 1)
print(filename)
filename_2 = getfpath(root='E:/分析项目/myself/爬取结果/CBM6_seq/',x = 5)


def dictfromlist(file,Evalueindex,Evaluethreshold,Idindex,Envfrom,Envto,file_2,newfp):
    with open(file) as yuanshi:
        reader = csv.reader(yuanshi)
        yuanshi_list = [i for i in reader]

    IDindexdict = {}
    for i in yuanshi_list:
        pass
        if float(i[Evalueindex]) <= Evaluethreshold:# 筛选i-Evalue符合条件的行
            index = i[Idindex]
            IDindexdict[index] = i[Envfrom] + ','+ i[Envto] + ','+ i[Evalueindex]
    print(IDindexdict)
# 第四步，从序列文件中抽提序列
    fasta = open(file_2, 'r')
    seq = {}  # 把总序列存入字典
    for i in fasta:
        if i.startswith('>'):
            o = i.split(" ", 1)[0]
            newid = o.strip('>')
            index = newid
            seq[index] = ''
        else:
            seq[index] += i.replace('\n', '')
    print(len(seq.keys()))
    shaixuanseq = {}
    for i in IDindexdict.keys():
        for p in seq.keys():
            if i.split("_", 1)[0] == p:
                num1 = int(IDindexdict[i].split(",", 2)[0])
                num2 = int(IDindexdict[i].split(",", 2)[1])
                id = '>' + i
                shaixuanseq[id] = seq[p][num1:num2]
    #print(shaixuanseq.items())
    print(len(IDindexdict.keys()))
    newfile = open(newfp, "w+")
    for k, v in shaixuanseq.items():
        newfile.write(k + '\n' + v + '\n')
dictfromlist(file=filename,Evalueindex=13,Evaluethreshold=0.01,Idindex=4,Envfrom=20,Envto=21,file_2=filename_2,newfp='E:/分析项目/myself/函数测试文件/pureCBMseq_CBM6比较多.txt')