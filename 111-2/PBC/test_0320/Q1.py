# Q1
a = int(input())
b = int(input())

if b%a == 0 :
    print(1,sep=',')
elif a%b == 0 :
    print(2,sep=',')
else:
    print(3,sep=',')