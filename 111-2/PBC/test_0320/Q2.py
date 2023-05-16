# Q2

n = int(input())

nit = input().split(',')
ni = []
for i in range(n+1):
    ni.append(int(nit[i]))

ans1 = 0  # 整除
ans2 = 0  # 沒整除
for i in range(1,n+1):
    if ni[i]%ni[0] == 0 :
        ans1 += 1
    else:
        ans2 += 1

if ans1 == 0 :
    print(1)
elif ans1 == 1 :
    print(2)
elif ans1 == n :
    print(3)
else:
    print(4)