# it returns 1,2,3 for 1d ,2d,3d array respectively
import numpy as np
ar_1d = np.array([1,2,3])
ar_2d = np.array([[1,2,3],[4,5,6]])
ar_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(ar_1d.ndim)  # Output: 1
print(ar_2d.ndim)  # Output: 2
print(ar_3d.ndim)  # Output: 3  
