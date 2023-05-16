# Q3

# read
n = int(input())  # n個車站
k = int(input())  # 載客人數
line3 = (input().split(','))
xn = []
for i in range(n):
    xn.append(int(line3[i]))

# 車站編號
nlist = []
for i in range(n):
    nlist.append(i+1)

# 總車數
if sum(xn)%k == 0:
    bus_num = sum(xn)//k
else:
    bus_num = sum(xn)//k

# 參數
onbus = [0] * len(xn)  # 已載客數
remain = 12  # 剩餘座位

# main
"""
for j in range(bus_num):
    onbus = [0] * len(xn)
    remain = k
"""
if remain < xn[i] and remain > 0:
        onbus[i] = (remain)
        xn[i] -= remain
        remain = 0

elif remain > xn[i] and remain > 0:
        onbus[i] = (xn[i])
        xn[i] = 0
        remain -= xn[i]

elif remain == 0:
        onbus[i] = (0)
        

print(remain)
