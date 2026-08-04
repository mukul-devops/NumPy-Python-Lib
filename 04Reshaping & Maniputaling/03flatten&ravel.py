'''
flatten() and ravel() are used to convert a multi-dimensional array into a one-dimensional array.
- flatten() always returns a copy of the array.
- ravel() returns a view of the array when possible, which is more memory efficient.
'''
import numpy as np
arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
x = arr_2d.flatten()   # Output: [1 2 3 4 5 6 7 8 9]
x[0] = 100
print(arr_2d)           # Output: [[  1  2   3 ]
                        #          [  4   5   6]
                        #          [  7   8   9]]


y = arr_2d.ravel()    # Output: [1 2 3 4 5 6 7 8 9]
y[0] = 100
print(arr_2d)         # Output: [[100   2   3]
                      #          [  4   5   6]
                      #          [  7   8   9]]