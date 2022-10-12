import argparse
import csv
import pandas as pd

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--fp', type=str, default=None)
parser.add_argument('--newf', type=str, default=None)
parser.add_argument('--addnumfn', type=str, default=None)
args = parser.parse_args()
print(args.fp)
print(args.newf)
print(args.addnumfn)


class ChangeSep(object):
    def __init__(self, fp, newfn, addnumfn):
        self.fp = fp
        self.newfn = newfn
        self.addnumfn = addnumfn

    def getfilepath(self):
        file = open(self.fp, 'r')
        newfile = open(self.newfn, "w")
        for i in file.readlines():
            newTxt = ""
            newTxt = newTxt + ",".join(i.split()) + "\n"
            print(newTxt)
            if newTxt.startswith('CBM'):
                newfile.write(newTxt)

        with open(newfile) as yuanshi:  # 打开序列ID文件
            reader = csv.reader(yuanshi)
            yuanshi_list = [i for i in reader]

        for i in range(len(yuanshi_list)):
            yuanshi_list[i][3] = yuanshi_list[i][3] + '#' + str(i)

        datasave = pd.DataFrame(yuanshi_list)
        datasave.to_csv(self.addnumfn)

        newfile.close()
        file.close()


def main():
    addnum = ChangeSep(args.fp, args.newf, args.addnumfn)
    addnum.getfilepath()


if __name__ == '__main__':
    main()
