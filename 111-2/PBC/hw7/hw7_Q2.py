# Hw6 for PBC
# Created on 20230418 by Tsai,C,Y
# Q1------------------------------------------------------------
# read input
path = input()
path2 = input()
word = ord(input())

# open file and creat dictionary
C2U = {}
with open(path, 'r') as file:
#with open('CNS_small7.txt', 'r') as file:  # CNS_small6.txt  allinone.txt
    for line in file:
        str1, str2 = line.strip().split('\t')
        cns = str1
        uni = int(str2, 16)  # turn unicode to int(10 base)
        if cns in C2U and uni != C2U[cns]:
            print('MAPPING_TABLE_ERROR')
            quit()
        elif cns not in C2U:
            C2U[cns] = uni

U2C = {}
for key in C2U:
    val = C2U[key]
    if val not in U2C:
        U2C[val] = [key]
    else:
        U2C[val].append(key)

cns_count = 0
C2P = {}
with open(path2, 'r') as file:
#with open('phonetic3.txt', 'r') as file:
    for line in file:
        cns, pin = line.strip().split('\t')

        if cns not in C2P :
            C2P[cns] = [pin]
            cns_count += 1

        elif cns in C2P:
            C2P[cns].append(pin)

print(cns_count)

try:
    cns_num = len(U2C[word])
except:
    print('NO_CNS_DATA')
    quit()

pinyen = []
try:
    for i in range(cns_num):
        for j in range(len(C2P[sorted(U2C[word])[i]])):
            pinyen.append(C2P[sorted(U2C[word])[i]][j])
except:
    print('NO_PHONETIC_DATA')
    quit()

total_out = []
for i in range(len((pinyen))):
    if pinyen[i] not in total_out:
        print(pinyen[i])
        total_out.append(pinyen[i])