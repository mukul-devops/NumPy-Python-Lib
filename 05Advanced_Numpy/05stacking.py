'''
np.vstack() and np.hstack() are used to stack arrays vertically and horizontally, respectively.
np.vstack(arrays)
np.hstack(arrays)
'''

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([5, 6, 7])
new_arr = np.vstack((arr1, arr2))
print(new_arr)  # Output: [[1 2 3]
                #          [5 6 7]]

new_arr = np.hstack((arr1, arr2))
print(new_arr)  # Output: [1 2 3 5 6 7]


d_arr1 = np.array([[1, 2, 3], 
                   [4, 5, 6]])
d_arr2 = np.array([[7, 8],
                   [10, 11]])
new_arr = np.hstack((d_arr1, d_arr2))
print(new_arr)  #output: [[ 1  2  3  7  8]
                #         [ 4  5  6 10 11]]

mix_arr = np.vstack((arr1, arr2, d_arr1))
print(mix_arr)  # Output: [[1 2 3]
                #          [5 6 7]
                #          [1 2 3]
                #          [4 5 6]]