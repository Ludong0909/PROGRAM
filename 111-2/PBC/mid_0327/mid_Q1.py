# Q1
line1 = (input().split(','))
n1 = int(line1[0])
n2 = int(line1[1])

line2 = (input().split(','))
p1 = []
for i in range(n1):
    p1.append(int(line2[i]))

line3 = (input().split(','))
p2 = []
for i in range(n2):
    p2.append(int(line3[i]))

p1ave = sum(p1)/len(p1)
p2ave = sum(p2)/len(p2)

if p1ave > p2ave:
    print(1)
elif p1ave < p2ave:
    print(2)
else:
    print(0)
