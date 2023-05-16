import numpy as np
import matplotlib.pyplot as plt

#numpy array
A = np.arange(4)
B = np.array([1,2,3])
print(A.shape)
C = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(C[:,2]) # the entire third column
print(C[0:2,0:2])  # first two column of the top two rows
D=np.zeros((2,3))  # 創造2x3的陣列

np.reshape
np.transpose
np.tile
np.hstack, np.vstack
np.columnstack

#numpy file
np.savetxt(fname, var, fmt='...', delimiter=' ', newline='\n', header='...', footer='...', comments='...')
np.loadtxt(fname, comments='...', skiprows=..., usecols=..., unpack=...)
np.fromfile(file, dtype=..., count=n)

#1D plot
plt.title('',fontsize=)
plt.xlabel('',fontsize=)
plt.ylabel('',fontsize=)
plt.text(, , '',fontsize=)
plt.xticks()
plt.yticks()
plt.xlim()
plt.ylim()
plt.xscale('log') 
plt.yscale('log')
plt.legend([],loc='location')

f, ax = plt.subplots(2,2,sharex='',sharey='')

#upper left
ax[0,0].set_xlim([])
ax[0,0].set_ylim([])
ax[0,0].set_xticks()
ax[0,0].set_yticks()
ax[0,0].set_title('',fontsize=)
ax[0,0].set_xlabel('',fontsize=)
ax[0,0].set_ylabel('',fontsize=)
ax[0,0].plot(,,'r--')
ax[0,0].legend([],loc='upper right')

#upper right
ax[0,1].set_xlim([])
ax[0,1].set_ylim([])
ax[0,1].set_xticks()
ax[0,1].set_yticks()
ax[0,1].set_title('',fontsize=)
ax[0,1].set_xlabel('',fontsize=)
ax[0,1].set_ylabel('',fontsize=)
ax[0,1].plot(,,'r--')
ax[0,1].legend([],loc='upper right')

#lower left
ax[1,0].set_xlim([])
ax[1,0].set_ylim([])
ax[1,0].set_xticks()
ax[1,0].set_yticks()
ax[1,0].set_title('',fontsize=)
ax[1,0].set_xlabel('',fontsize=)
ax[1,0].set_ylabel('',fontsize=)
ax[1,0].plot(,,'r--')
ax[1,0].legend([],loc='upper right')

#lower right
ax[1,1].set_xlim([])
ax[1,1].set_ylim([])
ax[1,1].set_xticks()
ax[1,1].set_yticks()
ax[1,1].set_title('',fontsize=)
ax[1,1].set_xlabel('',fontsize=)
ax[1,1].set_ylabel('',fontsize=)
ax[1,1].plot(,,'r--')
ax[1,1].legend([],loc='upper right')




