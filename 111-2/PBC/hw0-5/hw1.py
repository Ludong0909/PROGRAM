#HW1 for programming for business computing

#create by Tsai,C,Y in 20230304
""""
#1.
x1 = int(float(input()))
x2 = int(float(input()))
y1 = int(float(input()))
y2 = int(float(input()))
output1 = x1*2+x2*3
output2 = x1*4+x2*3

if output1%y1 == 0:
    output3 = int(output1/y1)
else:
    output3 = int(output1/y1+1)

if output2%y2 == 0:
    output4 = int(output2/y2)
else:
    output4 = int(output2/y2+1)

print(output1 , ',' , output2 , ',' , output3 , ',' , output4 , sep='')

#2.

#read the input data
x1 = int(float(input()))
x2 = int(float(input()))
y1 = int(float(input()))
y2 = int(float(input()))
p1 = int(float(input()))
p2 = int(float(input()))

#compute numbers of each products
egg = x1*2+x2*3
pineapple = x1*4+x2*3

#A. compute the numbers and costs using just type 1 employee
if (egg%y1 == 0):
    emp1_egg1 = egg//y1 
else:
    emp1_egg1 = egg//y1 + 1

if (pineapple%y2 == 0):
    emp1_pineapple1 = pineapple//y2 
else:
    emp1_pineapple1 = pineapple//y2 + 1

cost1 = (emp1_pineapple1 + emp1_egg1) * p1

#B. compute the numbers and costs using type 1 + 2 employee
if (0 < (egg%y1*y2 + pineapple%y2*y1) <= y1*y2):
    emp1_egg2 = egg//y1
    emp1_pineapple2 = pineapple//y2
    emp2 = 1
    cost2 = (emp1_pineapple2 + emp1_egg2) * p1 + emp2 * p2
else:
    cost2 = cost1

#choose the lower cost between two ways A and B
if (cost1 <= cost2):
    emp1_egg = emp1_egg1
    emp1_pineapple = emp1_pineapple1
    emp2 = 0
    cost = cost1
    print(egg  , pineapple  , emp1_egg  , emp1_pineapple , emp2 , cost , sep=',')
else:
    emp1_egg = emp1_egg2
    emp1_pineapple = emp1_pineapple2
    emp2 = 1
    cost = cost2
    print(egg  , pineapple  , emp1_egg  , emp1_pineapple , emp2 , cost , sep=',')
    
"""

#3.
# Created by Tsai,C,Y in 20230304
# Compute the lowest cost hiring employees  

# read the input data
x1 = int(float(input()))
x2 = int(float(input()))
y1 = int(float(input()))
y2 = int(float(input()))
p1 = int(float(input()))
p2 = int(float(input()))
r1 = int(float(input()))
r2 = int(float(input()))

# Compute numbers of each products
egg = x1 * 2 + x2 * 3
pineapple = x1 * 4 + x2 * 3

# Firstly, we use type 1 employee to get lowest cost. So compute type 1 emp. we need at least
# And the remaining must be delt with type 2 and 3 emp.
emp1_egg = egg // y1
emp1_pineapple = pineapple // y2

# If there is anything left
if (0 < (egg % y1 * y2 + pineapple % y2 * y1) <= y1 * y2):

    # There are four ways to produce:

    # A. All the left are made by type 2 emp.
    cost_A = (emp1_egg + emp1_pineapple) * p1 + p2

    # B. All the  left are made by type 3 emp.
    cost_B = (emp1_egg + emp1_pineapple) * p1 + egg % y1 * r1 + pineapple % y2 * r2

    # C. The left egg made by type 1, and the left pineapple made by type 3
    cost_C = (emp1_egg + 1 + emp1_pineapple) * p1  + pineapple % y2 * r2

    # D. Vice versa
    cost_D = (emp1_egg + emp1_pineapple + 1) * p1  + egg % y1 * r1

    # Finally, choose the lowest cost
    if ((cost_A <= cost_B) and (cost_A <= cost_C) and (cost_A <= cost_D)):
        cost = cost_A
    elif ((cost_B <= cost_A) and (cost_B <= cost_C) and (cost_B <= cost_D)):
        cost = cost_B
    elif ((cost_C < cost_A) and (cost_C < cost_B) and (cost_C < cost_D)):
        cost = cost_C
    else:
        cost = cost_D


# No left, which means we can use all type 1 emp. to get the lowest cost
else:
    cost = (emp1_egg + emp1_pineapple) * p1

# print output
print(egg, pineapple, cost, sep = ',')

cost = min(cost_A, cost_B, cost_C, cost_D)    
