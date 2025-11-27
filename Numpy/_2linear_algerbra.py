#matrix multiplication
import numpy
import numpy as np
a = np.full((2,2), 9)
b = np.full((2,3), 3)
i = np.identity(2)
print(np.matmul(a,b))

#get the determinant of matrix
c = np.random.randint(1,10,(3,3))
det_c = np.linalg.det(c)
print(det_c)

#.........
