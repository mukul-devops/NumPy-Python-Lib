'''
np.append(array, values, axis=None) is used to append new elements (also rows or columns) to an array.
'''
import numpy as np
arr_1d = np.array([1, 2, 3])
new_arr_1d = np.append(arr_1d, [4, 5, 6])
print(new_arr_1d)  # Output: [1 2 3 4 5 6]


arr = np.array([[1, 2, 3], 
                [4, 5, 6]])
new_arr = np.append(arr, [[7, 8, 9]], axis=0)
print(new_arr)  # Output: [[1 2 3]
                #          [4 5 6]
                #          [7 8 9]]