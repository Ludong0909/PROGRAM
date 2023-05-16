# Q3

# read
n = int(input())  # n個車站
k = int(input())  # 載客人數
line3 = (input().split(','))
x = []
for i in range(n):
    x.append(int(line3[i]))

# 車站編號
nlist = []
for i in range(n):
    nlist.append(i+1)

# 總車數
if sum(x)%k == 0:
    bus_num = sum(x)//k
else:
    bus_num = sum(x)//k

# 參數
onbus = [0] * len(x)  # 已載客數
r = k

# main

xn = [0]*len(x)
for i in range(len(x)):
    xn[i] = x[i]


for j in range(bus_num):
    r = k

    for i in range(len(xn)):

        if r < xn[i]:
            onbus[i] = (r)
            xn[i] -= r
            r = 0

        elif r > xn[i]:
            onbus[i] = (xn[i])
            r = (int(r - xn[i]))
            xn[i] = 0

        elif r == 0:
            onbus[i] = (0)
            r = 0

    print(onbus)
    print(xn)

    