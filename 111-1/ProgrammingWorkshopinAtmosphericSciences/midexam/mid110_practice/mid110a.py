import numpy as np
nb = 2
nt = 4
tree = [0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,]
treereshape = np.array(tree).reshape(6,7)
print(treereshape)

# Python Program to Generate Christmas Tree Pattern

# Generating Triangle Shape
def triangleShape(n):
    for i in range(n):
        for j in range(n-i):
            print('', end='0')
        for k in range(2*i+1):
            print('1',end='')
        print()

# Generating Pole Shape
def poleShape(n):
    for i in range(n):
        for j in range(n-1):
            print('0', end='')
        print('111')

# Input and Function Call
row = int(input('Enter number of rows: '))

triangleShape(row)
triangleShape(row)
poleShape(row)