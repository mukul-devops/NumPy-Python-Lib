'''
np.split() is used to split arrays into multiple sub-arrays.
np.split(array, indices_or_sections, axis=0)
array - The input array to be split.
indices_or_sections - The indices (like [2, 3] or [2]) or number of sections(like 2, 4) to split the array into.
axis - The axis along which to split the array. 0 for vertical split and 1 for horizontal split. Default is 0.
'''

import numpy as np
arr = np.array([1, 2, 3, 4])
new_arr = np.split(arr, 2)
print(new_arr)  # Output: [array([1, 2]), array([3, 4])]

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])  
new_arr_2d = np.split(arr_2d, [3], axis=0)
print(new_arr_2d)  # Output: [array([[1, 2, 3],
                   #                 [4, 5, 6],
                   #                 [7, 8, 9]]), array([[10, 11, 12]])]
                           
print(np.split(arr_2d, [1,2], axis=1))
# here [1,2] are the indices where the array will be split. 3 (section) also works same as [1,2] in this case. 
#output: [array([[1],
#                [4],
#                [7],
#                [10]]), array([[2],
#                [5],
#                [8],
#                [11]]), array([[3],
#                [6],
#                [9],
#                [12]])]