#creation of array from list   
import numpy as np
ar = np.array([34,65,45,23,65])
print(ar)

# with default values
#np.zeros(shape)      shape = (3)1d array, (3,4)2d array here 3 is the number of rows and 4 is the number of columns
ar_zeros = np.zeros(5)
print(ar_zeros)

#np.ones(shape) , create an array of ones   
ar_ones = np.ones((4,3))
print(ar_ones)  

#np.full(shape,fill_value)
ar_full = np.full((3,4),5)
print(ar_full)

#creating sequence of numbers in numpy
#np.arange(start,stop,step)
ar_range = np.arange(0, 10, 3)
print(ar_range)

#creating identity matrices
#np.eye(n) , n is the number of rows and columns
ar_eye = np.eye(3)
print(ar_eye)