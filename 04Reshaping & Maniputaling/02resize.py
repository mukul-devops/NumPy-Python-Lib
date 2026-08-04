 #Note: resize() changes the original array (as shape and size) and returns None.
import numpy as np
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12]])
arr.resize(2,6)
print(arr)     #output: [[ 1  2  3  4  5  6]
              #          [ 7  8  9 10 11 12]]


# arr.resize(3,3)
# print(arr)     #output: [[ 1  2  3]
              #          [ 4  5  6]
              #          [ 7  8  9]]

# arr.resize(4,5)
# print(arr)     #output: [[ 1  2  3  4  5]
              #          [ 6  7  8  9 10]
              #          [11 12  0  0  0]
              #          [ 0  0  0  0  0]]  