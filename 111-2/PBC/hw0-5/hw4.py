# Hw4 for PBC
# Created on 20230322 by Tsai,C,Y

# Q1---------------------------------------------------------------------
'''
# Read the data
n = int(input())

line1 = (input().split(','))
p1 = []
for i in range(n):
    p1.append(int(line1[i]))

line2 = (input().split(','))
p2 = []
for i in range(n):
    p2.append(int(line2[i]))


# Calculate 
# Set innitial value
assemble = []
wrapping = []
idleaccu = []
assemble.append(p1[0])
idleaccu.append(p1[0])

# Calculate idle time

for i in range(n-1):

    assemble.append(p1[i+1])
    wrapping.append(p2[i])

    if (sum(assemble)>sum(wrapping)+sum(idleaccu)):
        idleaccu.append(sum(assemble)-sum(wrapping) -sum(idleaccu))
    else:
        idleaccu.append(0)

    #print('ass = ',assemble)
    #print('wra = ',wrapping)
    #print('idl = ',idleaccu)


# Calculate produce time

producetime = 0
producelist = []
for i in range(n-1):
    producetime += (idleaccu[i] + wrapping[i])
    producelist.append(producetime)

producelist.append(producetime + p2[n-1] + idleaccu[n-1])

print(*producelist,sum(idleaccu),sep = ',')

# Q2--------------------------------------------------------------------

# Read the data
n = int(input())

line1 = (input().split(','))
p1 = []
for i in range(n):
    p1.append(int(line1[i]))

line2 = (input().split(','))
p2 = []
for i in range(n):
    p2.append(int(line2[i]))

p3 = []
for i in range(n):
    p3.append(p1[i] + p2[i])

p11 = [0]*n
p22 = [0]*n
p33 = [0]*n 
index = []
for i in range(n):
    index.append(i)
indexx = [0]*n

# Bubble sorting
for j in range(n):
    for i in range(n-1):
        if p3[i] > p3[i+1] :

            p33 [i] = p3[i+1]
            p33[i+1] = p3[i]
            p3[i] = p33[i]
            p3[i+1] = p33[i+1]

            p22 [i] = p2[i+1]
            p22[i+1] = p2[i]
            p2[i] = p22[i]
            p2[i+1] = p22[i+1]

            p11 [i] = p1[i+1]
            p11[i+1] = p1[i]
            p1[i] = p11[i]
            p1[i+1] = p11[i+1]

            indexx[i] = index[i+1]
            indexx[i+1] = index[i]
            index[i] = indexx[i]
            index[i+1] = indexx[i+1]

        elif p3[i] == p3[i+1] :
            if p1[i] > p1[i+1] :

                p33 [i] = p3[i+1]
                p33[i+1] = p3[i]
                p3[i] = p33[i]
                p3[i+1] = p33[i+1]

                p22 [i] = p2[i+1]
                p22[i+1] = p2[i]
                p2[i] = p22[i]
                p2[i+1] = p22[i+1]

                p11 [i] = p1[i+1]
                p11[i+1] = p1[i]
                p1[i] = p11[i]
                p1[i+1] = p11[i+1]

                indexx[i] = index[i+1]
                indexx[i+1] = index[i]
                index[i] = indexx[i]
                index[i+1] = indexx[i+1]
            
            elif p1[i] == p1[i+1]:
                continue
                #change?

        #print(j,i,'=',index)

#print(p1)
#print(p2)
#print(p3)
#print(index)   


# Calculate 
# Set innitial value
assemble = []
wrapping = []
idleaccu = []
assemble.append(p1[0])
idleaccu.append(p1[0])

# Calculate idle time

for i in range(n-1):

    assemble.append(p1[i+1])
    wrapping.append(p2[i])

    if (sum(assemble)>sum(wrapping)+sum(idleaccu)):
        idleaccu.append(sum(assemble)-sum(wrapping) -sum(idleaccu))
    else:
        idleaccu.append(0)

    #print('ass = ',assemble)
    #print('wra = ',wrapping)
    #print('idl = ',idleaccu)


# Calculate produce time

producetime = 0
producelist = []
for i in range(n-1):
    producetime += (idleaccu[i] + wrapping[i])
    producelist.append(producetime)

producelist.append(producetime + p2[n-1] + idleaccu[n-1])

# Sort the answer in toy number order
producelistsort = [0]*n
for i in range(n):
    producelistsort[index[i]] = (producelist[i])

print(*producelistsort,sum(idleaccu),sep = ',')


# Q3-------------------------------------------------------------------------
# Read the data
line1 = (input().split(','))
n = int(line1[0])  # 幾個玩具
m = int(line1[1])  # 幾條生產線

# Create a 2D array
produce_time = []
for i in range(m):
    lineafter = []
    line2 = (input().split(','))
    for j in range(n):
        lineafter.append(int(line2[j]))
    produce_time.append(lineafter)

# Calculate total time per type
worktime = []
for i in range(n):
    time = 0
    for j in range(m):
        time += produce_time[j][i]
    worktime.append(time)

# Bubble Sorting
# Sort index
index = []
indexx = []
for i in range(n):
    indexx.append(i)

for i in range(n):
    ind = -1
    minvalue = 9999
    for j in indexx:
        if worktime[j] < minvalue:
            ind = j
            minvalue = worktime[j]
        elif worktime[j] == minvalue:
            for k in range(m):
                if produce_time[k][j] < produce_time[k][ind]:
                    ind = j
                    minvalue = worktime[j]
                else:
                    break
    index.append(ind)
    indexx.remove(ind)


# Calculate 
# Set innitial value
totalidle = 0
time1 = []
time = []
time_line = 0
end = []

# Calculate idletime
for i in index:
    time_line += produce_time[0][i]
    time1.append(time_line)
    time.append(0)
    end.append(0)

for j in range(1,m):
    for i in range(n):
        if i == 0:
            idletime = time1[i]
            totalidle += idletime
            time[i] = time1[i] + produce_time[j][index[i]]
        else:
            if time1[i] > time[i-1]:
                idletime = time1[i] - time[i-1]
                totalidle += idletime
                time[i] = time[i-1] + idletime + produce_time[j][index[i]]
            else:
                time[i] = time[i-1] + produce_time[j][index[i]]

    for i in range(n):
        time1[i] = time[i]

# Sort back
for i in range(n):
    end[index[i]] = time[i]

# Print output
ans = str()
for i in range(n):
    ans += str(end[i]) + ','
ans += str(totalidle)
print(ans)
'''

# Hw4 for PBC
# Created on 20230401 by Tsai,C,Y
# This is so hard QAQ
# Q4------------------------------------------------------------------------------------

# 讀入階段
# 讀入第一行數據
line1 = (input().split(','))
toy = int(line1[0])  # 幾個玩具
line = int(float(line1[1]))  # 幾條生產線

# 讀入二維清單
produce_time = []
for i in range(line):
    lineafter = []
    line2 = (input().split(','))
    for j in range(toy):
        lineafter.append(int(line2[j]))
    produce_time.append(lineafter)


# 計算階段
# 建立記錄用的清單
# 記錄每條生產線的製造時間
time_eachline = [0] * line
time_eachline_record = [0] * line  # 記錄暫存的數據
totalidle = 0  #  累積時間

# 建立排序用的位置標籤
index = []
index_record = []  # 記錄暫存的標籤
for i in range(toy):
    index_record.append(i)
End_sorted = []  # 排序後
End = [0] * toy  # 原排序

# 排序順序(Bubble sort)
for j in range(toy):
    # 設定初始值
    minidle = 999
    minidle_index = -1

    # 找出最佳排序並記錄時間
    for i in index_record:
        idle_accumulate = 0

        # 計算並紀錄時間
        for k in range(line):
            if k == 0:
                time_eachline_record[k] = time_eachline[k] + produce_time[k][i]
            
            else:
                if time_eachline_record[k-1] > time_eachline[k]:
                    idletime = time_eachline_record[k-1] - time_eachline[k]
                    idle_accumulate += idletime
                    time_eachline_record[k] = time_eachline[k] + idletime + produce_time[k][i]
                
                else:
                    time_eachline_record[k] = time_eachline[k] + produce_time[k][i]

        if idle_accumulate < minidle:
            minidle = idle_accumulate
            minidle_index = i
    
    # 記錄每條生產線的時間
    for k in range(line):
        if k == 0:
            time_eachline[k] += produce_time[k][minidle_index]
        
        else:
            if time_eachline[k-1] > time_eachline[k]:
                idletime = time_eachline[k-1] - time_eachline[k]
                idle_accumulate += idletime
                time_eachline[k] = time_eachline[k] + idletime + produce_time[k][minidle_index]
                
            else:
                time_eachline[k] = time_eachline[k] + produce_time[k][minidle_index]
    
    # 記錄排序
    index.append(minidle_index)
    index_record.remove(minidle_index)
    totalidle += minidle
    End_sorted.append(time_eachline[-1])


# 輸出階段
# 將輸出時間按原順序排序
for i in range(toy):
    End[index[i]] = End_sorted[i]

# 輸出
output = str()
for i in range(toy):
    output += str(End[i]) + ','
output += str(totalidle)
print(output)