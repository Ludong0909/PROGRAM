# Q2
# read
line1 = (input().split(','))
M = int(line1[0])
R = int(line1[1])

line2 = (input().split(','))
n = []
for i in range(M):
    n.append(int(line2[i]))

line3 = (input().split(','))
q = []
for i in range(M):
    q.append(int(line3[i]))

xij = []
ave = []
for i in range(M):

    xj = []
    line4 = (input().split(','))
    for j in range(len(line4)):
        xj.append(int(line4[j]))
    while len(xj) == n:
        xj.append(0)
    xij.append(xj)
    avej = sum(xj)/len(xj)


    if ((q[i]/n[i]) >= R*0.01):
        ave.append(avej)
    else:
        ave.append(0)


# main

maxave = max(ave)
maxind = ave.index(max(ave))

if sum(ave) == 0:
    print(-1)
else:
    print(maxind+1,n[maxind],sum(xij[maxind]),sep=',')