#2023/02/20 Chih-Yen Tsai
#hw0 for Numerical Analysis
#Calculate n! value

def factorial (N):
    b = 1
    if (float(N)>=0.0): 
        if (float(N) == 0) : 
            return 1
        else:
            if (float(N)%1 == 0.0) :
                for i in range(1,int(float(N))+1):
	                b = b*i
                return b
            else: 
                print('the wrong input')
    else:
        print('the wrong input')