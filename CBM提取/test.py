#import re
import pandas as pd

result_1 = ">AJG17892.1 Alpha,alpha-trehalose-phosphate synthase [UDP-forming] [Cupriavidus basilensis]-glucoside)]"
result_1 = result_1.replace("[UDP-forming]","(UDP-forming)")
result_1 = result_1.split(" ", 1)

if "[[" in result_1[1]:
    result_2 = result_1[1].split("[[")
    print("它动了")
else:
    result_2 = result_1[1].split(" [")
    print("else动了")
result_2.insert(0, result_1[0])
result_2[-1] = result_2[-1].strip("]\n")
result_2[-1] = result_2[-1].replace("]","")
print(result_2)


test1026 = '>ADB61387.1#2,CBM9_1,Position:451-626'
result_1 = test1026.split(",", 2)
print(result_1)


