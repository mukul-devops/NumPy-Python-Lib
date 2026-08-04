'''
Indexing is used to access the single element of the array. The index can be a positive integer, negative integer.
array[index] #1d array
array[row,coloumn] #2d array
'''

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])  # Output: 1 (first element)
print(arr[2])  # Output: 3
print(arr[-1])  # Output: 5 (last element)

ar_2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(ar_2d[0,0])  # Output: 1 (first row, first column)
print(ar_2d[1,2])  # Output: 6 (second row, third column)
print(ar_2d[-1,-1])  # Output: 9 (last row, last column)