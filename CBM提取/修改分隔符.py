
import os



def getfilepath(root):
    filenames_list = os.listdir(root)
    filenamesall = []
    for i in filenames_list:
        filenamesall.append(root+i)
    return filenamesall
def getfilepath(root):
    filenames_list = os.listdir(root)
    filenamesall = []
    for i in filenames_list:
        filenamesall.append(root+i)
    return filenamesall

file = getfilepath(root='E:\\分析项目\\wxy\\wxy0920seq\\')

ls = open(file[0],'r')
print(file[0])

newfile = open('E:\\分析项目\\wxy\\wxy0920seq\\wxy0920seq_result_d.csv', "w")

for i in ls.readlines():

    newTxt = ""
    newTxt = newTxt + ",".join(i.split()) + "\n"
    print(newTxt)
    if newTxt.startswith('CBM'):
        pass
        newfile.write(newTxt)
newfile.close()
ls.close()









