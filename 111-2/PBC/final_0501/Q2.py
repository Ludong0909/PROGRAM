line1 = (input().split(','))
inlist = []
for i in range(len(line1)):
    inlist.append(float(line1[i]))
k1 =int(input())
k2 = int(input())

if k1 <= 0:
    k1 = 2
if k2 <= 0:
    k2 = 2


def find_troughs (inlist, k1 = 2, k2 = 2):
    '''
    Args:
        inlist: list = the input list,\n
        k: int

    '''
    out = []
    for i in range(k1,len(inlist)-k2):
            for j in range(k1):
                if inlist[i+j-k1] > inlist[i+j-k1+1]:
                    a = 1
                    
                else:
                    a = -1
                    break
            
            if a != 1:
                continue

            for j in range(k2):
                if inlist[i+j] < inlist[i+j+1]:
                    a = 1
                    
                else:
                    a = -1
                    break
            
            if a != 1:
                continue

            out.append(i)
    if len(out) == 0:
        return None
    else:
        return out
    
output = find_troughs(inlist ,k1, k2)

if output == None:
    print("NA")
else:
    for i in range(len(output)):
        print(output[i])