'''
isinf(array) is used to check for positive or negative infinity values in an array. 
It returns a boolean array of the same shape, where each element is True if the corresponding element in the input array is infinity, and False otherwise.
'''
import numpy as np
arr = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.isinf(arr))