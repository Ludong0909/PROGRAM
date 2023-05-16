from turtle import shape
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-1,1,5)
y = np.linspace(-1,1,4)
xx,yy = np.meshgrid(x,y)
z = np.exp(-np.sin(2*xx)-np.cos(2*yy))
print(xx.shape,yy.shape,z.shape)
print(xx)
print(yy)