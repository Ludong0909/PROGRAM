import math
import matplotlib.pyplot as plt

#read the n values to be calculated
f1=open('midb_input.txt','r')
ns=f1.readline()
nsf=[float(x) for x in ns.split(' ')]
ns=[round(x) for x in nsf]
f1.close()

# prepare output file
f2=open('mid109b.txt','w')
f2.write('# n        Sn     error\n')

for n in ns:
  if n>=0:
    # calculate Sn
    Sn=0
    for j in range(n+1):
      Sn = Sn +1/math.factorial(j)
    
    # Output result for each n
    f2.write('%3i%10f%10.2e\n' %(n,Sn,abs(Sn-math.exp(1))))
    # Plot results for each n
    plt.plot(n,abs(Sn-math.exp(1)),'bo')

f2.close()

# figure settings
plt.xscale('log')
plt.yscale('log')
plt.xticks([2,4,8,16,32],['2','4','8','16','32'])
plt.xlim([1,50])
plt.xlabel('n',fontsize=14)
plt.ylabel('error',fontsize=14)
plt.savefig('mid109b.png')
plt.show()