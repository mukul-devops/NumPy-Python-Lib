'''
np.isnan(array) is a function checks for NaN (Not a Number) values in an array. 
It returns a boolean array of the same shape as the input array, where each element is True if the corresponding element in the input array is NaN, and False otherwise.
'''
import numpy as np
arr = np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))


# print(np.nan == np.nan)  # cause error because np.nan is not defined