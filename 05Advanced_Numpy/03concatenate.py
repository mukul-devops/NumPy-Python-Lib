'''
concatenate(arrays, axis=0, out=None) function is used to join two or more arrays of the same shape along a specified axis.
arrays - (arr1,arr2,...) sequence of arrays to be joined
axis - axis along which the arrays are joined (default is 0)
out - output array (optional) 
'''
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
new_arr = np.concatenate((arr1, arr2)) 
print(new_arr)  


arr1 = np.array([[1, 2], 
                 [3, 4]])
arr2 = np.array([[5, 6],
                 [7, 8]])
new_arr = np.concatenate((arr1, arr2), axis=1)
print(new_arr)