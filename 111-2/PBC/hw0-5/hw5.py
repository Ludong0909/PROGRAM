# Hw5 for PBC
# Created on 20230404 by Tsai,C,Y
# Q1------------------------------------------------------------

line1 = (input().split(','))
inlist = []
for i in range(len(line1)):
    inlist.append(float(line1[i]))
input = int(input())

if input > 0:
    k = input
else:
    k = 2



def find_troughs (inlist, k = 2):
    '''
    Args:
        inlist: list = the input list,\n
        k: int

    '''
    out = []
    for i in range(k,len(inlist)-k):
            for j in range(k):
                if inlist[i+j-k] > inlist[i+j-k+1]:
                    a = 1
                    
                else:
                    a = -1
                    break
            
            if a != 1:
                continue

            for j in range(k):
                if inlist[i+j] < inlist[i+j+1]:
                    a = 1
                    
                else:
                    a = -1
                    break
            
            if a != 1:
                continue

            out.append(i)
    if len(out) == 0:
        return None
    else:
        return out

output = find_troughs(inlist,k)

if output == None:
    print("NA")
else:
    for i in range(len(output)):
        print(output[i])

# Q2------------------------------------------------------------

line1 = (input().split(','))
inlist = []
for i in range(len(line1)):
    inlist.append(float(line1[i]))
input = int(input())

if input > 0:
    k = input
else:
    k = 2

def find_troughs_wings (inlist, k = 2):
    '''
    Args:
        inlist: list = the input list,\n
        k: int

    Return:
        out: list or None
    '''
    out = []
    for i in range(k+1,len(inlist)-k-1):
            b = 0
            if inlist[i-k-1] < inlist[i-k]:
                b = 1

            for j in range(k):
                if inlist[i+j-k] > inlist[i+j-k+1]:
                    a = 1
                    
                else:
                    a = -1
                    break
            
            if a != 1 or b != 1:
                continue
            b = 0
            for j in range(k):
                if inlist[i+j] < inlist[i+j+1]:
                    a = 1
                    
                else:
                    a = -1
                    break
            
            if inlist[i+k] > inlist[i+k+1]:
                b = 1

            if a != 1 or b != 1:
                continue

            out.append(i)
    if len(out) == 0:
        return None
    else:
        return out
    
output = find_troughs_wings(inlist,k)

if output == None:
    print("NA")
else:
    for i in range(len(output)):
        print(output[i])

# Q3---------------------------------------------------------------
# Read input
n = int(input())
stop = 0
edge = []
while True:
    line = (input())
    if line == 'STOP':
        break
    values = line.split(',')
    pair = []
    for i in range(len(values)):
        pair.append(int(values[i]))
    edge.append(pair)

# Calculate minimum dimension of array
maxval = []
for i in range(len(edge)):
    maxval.append(max(edge[i]))
if len(maxval) != 0:
    k = max(maxval) + 1
else:
    k = 0

# Write edge in array then print output
if n == 0 :
    n = k
    array = []
    for i in range(n):
        array.append([0]*n)
    for i in range(len(edge)):
        array[edge[i][0]][edge[i][1]] = 1
        array[edge[i][1]][edge[i][0]] = 1
    for i in range(len(array[1])):
        print(*array[i],sep=',')
elif n < k:
    print('None')
elif n >= k:
    array = []
    for i in range(n):
        array.append([0]*n)
    for i in range(len(edge)):
        array[edge[i][0]][edge[i][1]] = 1
        array[edge[i][1]][edge[i][0]] = 1
    for i in range(len(array[1])):
        print(*array[i],sep=',')

# Q4---------------------------------------------------------------

n = int(input())
k = int(input())

edge = []
while True:
    line = (input())
    if line == 'STOP':
        break
    values = line.split(',')
    pair = []
    for i in range(len(values)):
        pair.append(int(values[i]))
    edge.append(pair)

def to_adj_mat (edge,n=0):
    # Calculate minimum dimension of array
    maxval = []
    for i in range(len(edge)):
        maxval.append(max(edge[i]))
    if len(maxval) != 0:
        k = max(maxval) + 1
    else:
        k = 0

    # Write edge in array
    if n == 0 :
        n = k
        array = []
        for i in range(n):
            array.append([0]*n)

        for i in range(len(edge)):
            array[edge[i][0]][edge[i][1]] = 1
            array[edge[i][1]][edge[i][0]] = 1
        return array

    # Print output
    elif n < k:
        return None

    elif n >= k:
        array = []
        for i in range(n):
            array.append([0]*n)
        for i in range(len(edge)):
            array[edge[i][0]][edge[i][1]] = 1
            array[edge[i][1]][edge[i][0]] = 1
        return array

adj_mat = to_adj_mat(edge,n)

if adj_mat == None:
    print('None')
else:
    # 判斷是否超出範圍
    if k >= len(adj_mat[0]):
        print('None')
    else:   
        # 找出鄰接節點
        node_location = []
        for i in range(len(adj_mat[0])):
            if adj_mat[k][i] == 1:
                node_location.append(i)

        #print(node_location)

        # 找出有最多共同節點的點
        n_node = []
        for i in range(len(adj_mat[0])):
            nn = 0
            for m in node_location:
                if adj_mat[i][m] == 1:
                    nn += 1
            n_node.append(nn)  # 共同節點數(長度為array[0]的一維清單,表示主角與n的共同節點數)


        n_node[k] -= 100

        #for i in range(len(n_node)):
        where = n_node.index(max(n_node))
        print(where)
        print(n_node[where])