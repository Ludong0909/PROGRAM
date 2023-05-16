# Hw6 for PBC
# Created on 20230418 by Tsai,C,Y
# Q1------------------------------------------------------------
# read input
path = input()
input = input()

# judge condition
if input[0:5] == 'CHAR:' :
    condition = 1
else:
    condition = 2

# open file
# CNS2UNICODE_Unicode BMP.txt
# CNS_small3.txt
uni_value = []
uni_key = []
cns_value = []
cns_key = []
#with open('CNS_small3.txt', 'r') as file:
with open(path, 'r') as file:
    for line in file:
        string1, string2 = line.strip().split('\t')
        cns_value.append([string1])
        cns_key.append(string1)
        uni_value.append([string2])
        uni_key.append(string2)