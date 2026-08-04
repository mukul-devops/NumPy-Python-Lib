'''
vectorization is a programming technique that allows you to perform operations on entire arrays or sequences of data at once, rather than using explicit loops to iterate through individual elements.
it is a key feature of numpy and other numerical computing libraries, enabling efficient and concise code for mathematical and scientific computations.
differce between vectorization and broadcasting:
Broadcasting = Makes arrays of different shapes compatible for operations. Broadcasting is about shape compatibility.
Vectorization = Performs operations on entire arrays without writing Python loops. Vectorization is about speed.
'''
#using list comprehension
list1 = [1,2,3,4]
list2 = [5,6,7,8]
result = [a + b for a, b in zip(list1, list2)]
print(result)  # Output: [6, 8, 10, 12]

#using vectorization
import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
result = arr1 + arr2
print(result)  # Output: [ 6  8 10 12]

new_arr1 = arr1**2
print(new_arr1)  # Output: [ 1  4  9 16]