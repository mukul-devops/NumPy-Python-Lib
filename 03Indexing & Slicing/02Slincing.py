#array[start:end:step]  
#slicing is used to access a range of elements in an array
import numpy as np
array = np.array([10,20,30,40,50])
print(array[0:4])  # Output: [10 20 30 40]
print(array[:3])   # Output: [10 20 30]
print(array[::2])  # Output: [10 30 50]
print(array[::-1]) # Output: [50 40 30 20 10] for reversing the array step is -1. Default value of step is 1.
