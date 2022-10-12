import pandas as pd
import argparse
import csv

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--fp', type=str, default=None)
parser.add_argument('--newf', type=str, default=None)
parser.add_argument('--addnumfn', type=str, default=None)
parser.add_argument('--Evalueindex', type=int, default=13)
parser.add_argument('--Evaluethreshold', type=int, default=0.01)
parser.add_argument('--Idindex', type=int, default=4)
parser.add_argument('--Envfrom', type=int, default=20)
parser.add_argument('--Envto', type=int, default=21)
parser.add_argument('--seqfile', type=str, default=None)
parser.add_argument('--extracted', type=str, default=None)
args = parser.parse_args()
print(args.fp)
print(args.newf)
print(args.addnumfn)


class ExtractTextbyLocation(object):
    def __init__(self, fp, newfn, addnumfn):
        self.fp = fp  # hmmscan分析输出的原始结果文件
        self.newfn = newfn  # 修改分隔符之后的文件
        self.addnumfn = addnumfn  # GenbankAccession加上数字后缀的结果文件，也是为文本提取提供文本位置的输入文件。

    def ChangeSepandAddNum(self):
        """
        修改文件分隔符，给GenbankAccession加数字后缀，防止重复
        """
        file = open(self.fp, 'r')
        newfile = open(self.newfn, "w")
        for i in file.readlines():
            newTxt = ""
            newTxt = newTxt + ",".join(i.split()) + "\n"
            print(newTxt)
            if newTxt.startswith('CBM'):
                newfile.write(newTxt)

        with open(self.newfn) as yuanshi:  # 打开序列ID文件
            reader = csv.reader(yuanshi)
            yuanshi_list = [i for i in reader]

        for i in range(len(yuanshi_list)):
            yuanshi_list[i][3] = yuanshi_list[i][3] + '#' + str(i)

        datasave = pd.DataFrame(yuanshi_list)
        datasave.to_csv(self.addnumfn)

        newfile.close()
        file.close()

    def ExtractText(self, Evalueindex, Evaluethreshold, Idindex, Envfrom, Envto, file_2, newfp):
        """
        根据位置做文本提取，将提取的结果输出到新的文件中

        :param Evalueindex: 文件中记录hmmscan分析给出的与数据库中的结构域相似的显著性值的列
        :param Evaluethreshold: 设置显著性值的阈值
        :param Idindex: 文件中记录GenbankAccession的列
        :param Envfrom: 文件中记录CBM位置起始值的列
        :param Envto:   文件中记录CBM位置结束值的列
        :param file_2:  待提取文本的总序列文件
        :param newfp:   结果文件
        :return:    无返回值
        """
        with open(self.addnumfn) as yuanshi:
            reader = csv.reader(yuanshi)
            yuanshi_list = [i for i in reader]

        IDindexdict = {}
        for i in yuanshi_list:
            pass
            if float(i[Evalueindex]) <= Evaluethreshold:  # 筛选i-Evalue符合条件的行
                index = i[Idindex]  # + ',' +i[1]
                IDindexdict[index] = i[Envfrom] + ',' + i[Envto] + ',' + i[Evalueindex]
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
                if i.split("#", 1)[0] == p:
                    num1 = int(IDindexdict[i].split(",", 2)[0])
                    num2 = int(IDindexdict[i].split(",", 2)[1])
                    id = '>' + i
                    shaixuanseq[id] = seq[p][num1 - 1:num2]
        # print(shaixuanseq.items())
        print(len(IDindexdict.keys()))
        newfile = open(newfp, "w+")
        for k, v in shaixuanseq.items():
            newfile.write(k + '\n' + v + '\n')


def main():
    '''
    args.fp:hmmscan分析输出的原始结果文件
    args.newf:修改分隔符之后的结果文件
    args.addnumfn:enbankAccession加上数字后缀的结果文件，也是为文本提取提供文本位置的输入文件

    args.Evalueindex:'--Evalueindex', type=int, default=13
    args.Evaluethreshold:'--Evaluethreshold', type=int, default=0.01
    args.Idindex:'--Idindex', type=int, default=4
    args.Envfrom:
    args.Envto:
    args.seqfile:待提取文本的总序列文件
    args.extracted:结果文件

    :return:
    '''
    one = ExtractTextbyLocation(args.fp, args.newf, args.addnumfn)

    one.ChangeSepandAddNum()
    one.ExtractText(args.Evalueindex, args.Evaluethreshold, args.Idindex,
                    args.Envfrom, args.Envto, args.seqfile, args.extracted)


if __name__ == '__main__':
    main()

"""
 python3 ExtractTextbyLocation.py --fp /home/www/CBMSeqDownload/HmmProj/hmmscanresult/CBM10.csv --newf ./CBM10sep.csv --addnumfn ./CBM10addnum.csv --seqfile /home/www/CBMSeqDownload/CBMAASeqDownload/Download20210918/CBM10.fasta --extracted ./CBM10output.fasta
"""
