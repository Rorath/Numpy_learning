import numpy as np
#load data from .txt file
a = np.genfromtxt('Data.txt', delimiter=',')
print(a)#data is stored as float by default
print(a.astype(int))#change it into int

