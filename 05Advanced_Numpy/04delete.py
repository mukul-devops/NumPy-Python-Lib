'''
np.delete(arr, obj, axis=None) is used to delete elements from an array along a specified axis.
arr - input array
obj - index or indices of elements to delete
axis - axis along which to delete (default is None, which flattens the array)
'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
new_arr = np.delete(arr, 2)  # Delete element at index 2
print(new_arr)               # Output: [1 2 4 5]

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
new_arr_2d = np.delete(arr_2d, 1, axis=0)  # Delete row at index 1
print(new_arr_2d)                          # Output: [[1 2 3]
                                           #          [7 8 9]]