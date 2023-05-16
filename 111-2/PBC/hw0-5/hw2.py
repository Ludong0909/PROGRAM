# HW2 for programming for business computing

# create by Tsai,C,Y in 20230308
import pycodestyle
"""
# Q1.
n = int(input())
y = 0

for i in range(n):
    x = int(input())
    y = y+x
    if y < 0 :
        print(i+1)
        break

if y >= 0:
    print(y)


# Q2.

n = int(input())
pineapple_n = 0
egg_n = 0

for i in range(n):
    x = int(input())
    pineapple = x*((i+1)+2)
    egg = x*(i+1)
    pineapple_n += pineapple
    egg_n += egg

y1 = int(input())
y2 = int(input())

if egg_n%y2 ==0:
    staff2 = egg_n//y2
else:
    staff2 = egg_n//y2+1

if pineapple_n%y1 ==0:
    staff1 = pineapple_n//y1
else:
    staff1 = pineapple_n//y1+1

print(pineapple_n,egg_n,staff1,staff2,sep=',')
"""

# Q3.

# 讀入並賦值
order_days = int(input())  # m 表示未來的訂單天數
amount_increase = int(input())  # b 表示每天增加的量
phoneix_box = int(input())  # x1 表示第一天的鳳黃禮盒數量
traditional_box = int(input())  # x2 表示第一天的傳統禮盒數量
pineapple_work = int(input())  # y1 表示一個員工一天內可製作的鳳梨酥數量
egg_work = int(input())  # y2 表示一個員工一天內可製作的蛋黃酥數量


# 設定第0天的禮盒初始值為0
phoneix_total = 0
traditional_total = 0

# 利用迴圈進行計算
# 迴圈計算範圍設定為未來訂單天數
for i in range(order_days):
    # 計算未來第 i + 1 天時的禮盒總量
    phoneix_total = phoneix_box + (i) * amount_increase
    traditional_total = traditional_box + (i) * amount_increase

    # 計算禮盒內的糕點總量
    egg_total = phoneix_total * 2 + traditional_total * 3
    pineapple_total = phoneix_total * 4 + traditional_total * 3

    # 計算聘請的員工數量，若無法整除則須無條件進位
    if (egg_total % egg_work == 0):
        egg_staff = egg_total // egg_work
    else:
        egg_staff = egg_total // egg_work + 1

    if (pineapple_total % pineapple_work == 0):
        pineapple_staff = pineapple_total // pineapple_work
    else:
        pineapple_staff = pineapple_total // pineapple_work + 1

    # 輸出答案
    print(pineapple_staff, egg_staff, sep=',')