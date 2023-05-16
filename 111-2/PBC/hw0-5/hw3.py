# Hw3 for PBC
# Created on 20230314 by Tsai,C,Y

# Q1---------------------------------------------------------------------

# Read the input
line1 = (input().split(','))
n = int(line1[0])
x = int(line1[1])
line2 = (input().split(','))
p = []
for i in range(n):
    p.append(int(line2[i]))
line3 = (input().split(','))
L = int(line3[0])
U = int(line3[1])
y = 0

for i in range(n-1):

    if (p[i] <= L):
        y += (x // 2 // p[i])
        x -= (x // 2 // p[i]) * p[i]
    elif (L < p[i] < U):
        x = x
        y = y
    elif (p[i] >= U):
        x += (y // 2) * p[i]
        y -= y // 2 

x += y * p[-1]
y -= y

print(x)



# Q2--------------------------------------------------------------

# Read the input
line1 = (input().split(','))
n = int(line1[0])
m = int(line1[1])
x0 = int(line1[2])

line2 = (input().split(','))
L = []
for i in range(m):
    L.append(int(line2[i]))

line3 = (input().split(','))
U = []
for i in range(m):
    U.append(int(line3[i]))

line4 = (input().split(','))
p = []
for i in range(n):
    p.append(int(line4[i]))

y = 0
money = []

for j in range(m):
    #print(j)
    x = x0
    y = 0
    for i in range(n-1):
        if (p[i] <= L[j]):
            y += (x // 2 // p[i])
            x -= (x // 2 // p[i]) * p[i]
            #print(x,y)
        elif (L[j] < p[i] < U[j]):
            x = x
            y = y
            #print('Nothing')
        elif (p[i] >= U[j]):
            x += (y // 2) * p[i]
            y -= y // 2
            #print(x,y)
    x += y * p[-1]
    #print(x)
    money.append(x)

max = max(money)
print(max)



# Q3-----------------------------------------------------------------

# Read input
line1 = (input().split(','))
m = int(line1[0])
y1 = int(line1[1])
y2 = int(line1[2])

line2 = (input().split(','))
D1 = []
for i in range(m):
    D1.append(int(line2[i]))

line3 = (input().split(','))
D2 = []
for i in range(m):
    D2.append(int(line3[i]))

people = str()
for i in range(m):
    if (4 * D1[i] + 3 * D2[i]) % y1 == 0 :
        pine_people = ((4 * D1[i] + 3 * D2[i]) // y1)
    else:
        pine_people = ((4 * D1[i] + 3 * D2[i]) // y1) + 1

    if ((2 * D1[i] + 3 * D2[i]) % y2) == 0 :
        egg_people = ((2 * D1[i] + 3 * D2[i]) // y2)
    else:
        egg_people = ((2 * D1[i] + 3 * D2[i]) // y2) +1
    people += str(pine_people + egg_people) + ','

print(people[0:-1])



# Q4-------------------------------------------------------------

# 讀取並轉換前三行資料
# 第一行資料
line1 = input().split(',')
gifttype = int(line1[0])  # n種禮盒
day_of_order = int(line1[1])  # 未來m天的計算量
pineapple_workload = int(line1[2])  # 可做y1個鳳梨酥
egg_workload = int(line1[3])  # 可做y2個蛋黃酥

# 第二行資料, x11~xn1
line2 = input().split(',')
pineapple = []
for i in range(gifttype):
    pineapple.append(int(line2[i]))

# 第三行資料, x12~xn2
line3 = input().split(',')
egg = []
for i in range(gifttype):
    egg.append(int(line3[i]))

# 第四行資料開始須使用迴圈讀成二維清單
demand = []
for i in range(gifttype):

    line_after3 = input().split(',')  # 讀入第三行之後的資料
    demand_i = []  # Di1~Dim 未來m天的第i種禮盒需求量
    for j in range(day_of_order):
        demand_i.append(int(line_after3[j]))

    demand.append(demand_i)  # 將讀入的清單再併入，形成二維清單

# 使用巢狀迴圈計算各糕餅每天的需求量，並以清單形式儲存
pineapple_total = []
egg_total = []
for i in range(day_of_order):  #未來m天的訂單
    pineapple_number = 0
    egg_number = 0

    for j in range(gifttype):  #當天須製作的量
        pineapple_number += (pineapple[j] * demand[j][i])
        egg_number += (egg[j] * demand[j][i])

    # 將結果併入清單
    pineapple_total.append(pineapple_number)
    egg_total.append(egg_number)

# 計算分別所需要的人數，並併入清單
worker_pineapple = []
worker_egg = []
for i in range(day_of_order):

    # 判斷是否整除
    if (pineapple_total[i] % pineapple_workload == 0):
        worker_pineapple.append(pineapple_total[i] // pineapple_workload)
    else:
        worker_pineapple.append(pineapple_total[i] // pineapple_workload + 1)

    if (egg_total[i] % egg_workload == 0):
        worker_egg.append(egg_total[i] // egg_workload)
    else:
        worker_egg.append(egg_total[i] // egg_workload + 1)


# 加總鳳梨酥與蛋黃酥每日所需工人數，並以字串形式輸出（為了符合輸出規定，故採用字串形式輸出）
worker = str()
for i in range(day_of_order):
    worker += str(worker_pineapple[i] + worker_egg[i]) + ','

# 輸出結果
print(worker[0:-1])