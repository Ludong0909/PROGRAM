import numpy as np
import ASNumericalAnalysisFunc as NAf

def TaylerExpensionCos(x,term):
    cos = np.zeros(term)
    cos = np.array(cos,dtype=np.float64)
    cos[0] = 1
    for i in range(term-1):
        cos[i+1] = cos[i] + (-1)**(i+1)*x**(2*(i+1))/NAf.Factorial(2*(i+1))

    return cos

cos = TaylerExpensionCos(np.pi/3,8)
print(cos)

cos1 = 1
cos2 = (np.pi/3)**2/2
cos3 = (np.pi/3)**4/24
cos_round = round(cos1,6)-round(cos2,6)+round(cos3,6)
print(cos_round)


relative = abs(cos_round-0.5)/0.5
print(relative*100)