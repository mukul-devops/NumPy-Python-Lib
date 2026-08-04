# aggregation functions are used to perform operations on arrays and return a single value as a result. These functions are commonly used in data analysis and scientific computing to summarize or extract information from arrays.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))  # Output: 15
print(np.mean(arr))  # Output: 3.0
print(np.std(arr))  # Output: 1.4142135623730951
print(np.var(arr))  # Output: 2.0
print(np.min(arr))  # Output: 1
print(np.max(arr))  # Output: 5
print(np.median(arr))  # Output: 3.0
print(np.prod(arr))  # Output: 120 (product of all elements)
print(np.argmax(arr))  # Output: 4 (index of maximum value)
print(np.argmin(arr))  # Output: 0 (index of minimum value)
print(np.cumsum(arr))  # Output: [ 1  3  6 10 15] (cumulative sum)
print(np.cumprod(arr))  # Output: [  1   2  6  24 120] (cumulative product)
