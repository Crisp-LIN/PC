file_2="E:\\code\\Python\\CBM提取\\1.txt"
newfp = "E:\\code\\Python\\CBM提取\\2.txt" 
seq = {}
fasta = open(file_2, 'r')
seq = {}  # 把总序列存入字典
for i in fasta:
    if i.startswith('>'):
        o = i.strip("\n")
        index = o
        seq[index] = ''
    else:
        seq[index] += i.replace('\n', '')
print(seq.keys())
newfile = open(newfp, "w+")
for k, v in seq.items():
    newfile.write(k + '\n' + v + '\n')