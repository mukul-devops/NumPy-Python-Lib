import numpy as np
#reshape is used to change the shape of an array without changing its data and it returns a new array with the specified shape. The total number of elements in the new array must be the same as the original array. 
arr = np.arange(2,14)    #it returns [2 3 4 5 6 7 8 9 10 11 12 13]
print(arr.reshape(3,4)) 


arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12]])
print(arr.reshape(1,12))

 