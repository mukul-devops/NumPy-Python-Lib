'''
np.insert(array, index, value, axis=None) is used to insert a new element (also a row or column) in an array at a specified index.
array - original array
index - [2] index where the new element is to be inserted
value - [54] OR [13,14,15,16] new element(s) to be inserted
axis - [0] axis along which the new element is to be inserted 
(0 for row, 1 for column, default is None(None means the array is flattened before insertion))
'''
import numpy as np
arr = np.array([1,2,3,4,5])
new_arr= np.insert(arr, 4, 54)
print(new_arr)

#np.insert() is used to insert a new row or column in a 2D array
arr_2d = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])
new_2d_arr = np.insert(arr_2d, 3, [13,14,15,16], axis = 0) 
print(new_2d_arr)
                        
print(arr_2d) # original array remains unchanged