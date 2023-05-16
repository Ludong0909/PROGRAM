# Hw6 for PBC
# Created on 20230418 by Tsai,C,Y
# Q1------------------------------------------------------------
# read input
path = input()
input = input().split(':')
word = input[1]

# judge condition
if input[0] == 'CNS' :
    condition = 1
else:
    condition = 2

# open file
C2U = {}
cns_count = 0
with open(path, 'r') as file:
    for line in file:
        str1, str2 = line.strip().split('\t')
        cns = str1
        uni = int(str2, 16)  # turn unicode to int(10 base)
        if cns in C2U and uni != C2U[cns]:
            print('MAPPING_TABLE_ERROR')
            quit()
        elif cns not in C2U:
            C2U[cns] = uni
            cns_count += 1
print(cns_count)

U2C = {}
for key in C2U:
    val = C2U[key]
    if val not in U2C:
        U2C[val] = [key]
    else:
        U2C[val].append(key)

found = False
if condition == 1:  # word is a CNS
    if word in C2U:
        found = True
        output = chr(C2U[word])
        print(output)
else:  # word is a chinese word
    if ord(word) in U2C:
        found = True
        output = U2C[ord(word)]
        output.sort()
        for i in range(len(output)):
            print(output[i])

if not found:
    print("NO_DATA_FOUND")