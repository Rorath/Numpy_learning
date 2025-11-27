import numpy as np

arr = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])
print(np.shape(arr))
#min
print(np.min(arr))#find the minimum
print(np.min(arr, axis=0))#(2,2,3) the 0th element is removed, only reserve the
#minmym one ------> 2x3
print(np.max(arr, axis=1))#2,2,3) the 1st element is removed, only reserve the
#minmym one ------> 2x3
print(np.max(arr, axis=2))#2,2,3) the 2nd element is removed, only reserve the
#minmym one ------> 2x2

b = np.ones((3,3))
print(np.sum(b))

#size is the number of entries and shape is the layout of matrix
#as long as the size is the same, we can use before.reshape()
c = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(np.size(c))
print(c.reshape((2,9)))

a = np.array([[1],[2],[3]])
b = np.array([[2],[3],[4]]) + 2
# print(np.array([a,b]))#error reported
print(np.vstack((a,b))) #axis 0 should be the same
#np.vstack is more like an extension (Extends along the first axis)
print(np.hstack((a,b)))#axis 1 should be the same

#important things about axis
#       a x b x c x d
#axis   0   1   2   3

c = np.random.randint(1,10,(3,4))
print(c)
print(c > 3)# return a matrix with same size but only boolean value
print(c[c>3])#return all the entries that statisfy the condition
print(c[[0,2]])# index with a list in NumPY

#see if all or any of an element on an axis satisfying the condition
d = np.random.randint(1,9,(3,4))
print(d)
print(np.any(d>3,axis=0))
print(np.all(d>3,axis=1))

e = np.array([[i+j*5 for i in range(1,6)] for j in range(6)])
print(e[2:4,0:2])
print(e[[0,1,2,3],[1,2,3,4]])
print(e[[0,4,5],3:5])