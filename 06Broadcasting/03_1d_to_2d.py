import numpy as np

matrix = np.array([[1,2,3],  #(2,3)matrix
                [4,5,6]])
vector = np.array([1,2,3])   # (3,) vector , if vector is (2,) then it will throw error because of shape mismatch
result = matrix + vector
print(result)  # Output: [[2 4 6]
               #          [5 7 9]]

