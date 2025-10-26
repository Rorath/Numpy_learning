import numpy as np
a = np.array([1, 2, 3])
counter =1
grid = []
for i in range(3):
    grid.append([])
    for j in range(3):
        grid[i].append([])
        for _ in range(3):
            grid[i][j].append(counter)
            counter += 1
b = np.array(grid)
print(b.shape, b.ndim)
print(b[:])

c = np.zeros((3, 3, 3))
print(c)

d = np.full((3, 3, 3), 9)# inside the first parameter is
# the shape
print(d)

e = np.full_like(d, -1)# the first parameter is an np.array
print(e)

#generate float between 0 to 1
f = np.random.rand(3, 3, 3)
g = np.random.random_sample((3, 3, 3))
print(f,g)
#both of them works but random need a size in tuple while rand only size
#breaking down into separated parameters

#generate int exclusively first parameter is lower boundary
#second is higher boundary, the third parameter is size(tuple)
j = np.random.randint(0,9,(3,3,3))
print(j)

#identity matrx
k = np.identity(3)
print(k)

#np.array also preserves mutable so be careful about mutable and immutable
#a = b means a and b referring to same list
#a = b.copy() create a shallow copy

#+ - * / // %
l = np.array([1,2,3]); m = np.array([4,5,6])
print(l+2)
print(l%2)
l += m
print(l)
