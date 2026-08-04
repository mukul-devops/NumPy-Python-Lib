#filtering is used to extract elements from an array based on a condition. It is also known as boolean masking. It returns a new array containing only the elements that satisfy the condition.
import numpy as np 
array = np.array([1, 2, 3, 4, 5])
print(array[array > 3])  # Output: [4 5]