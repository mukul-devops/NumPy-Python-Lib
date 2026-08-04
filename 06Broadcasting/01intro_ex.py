'''
broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes and dimensions when performing arithmetic operations without the need for explicit replication of data.
it is very fast and memory efficient as it avoids unnecessary data duplication. loops are avoided and operations are performed in a vectorized manner, which is a key feature of numpy.

rules of broadcasting:
1. Matching dimensions: If arrays have same dimentions , [1,2,3] + [4,5,6] = [5,7,9]
If the arrays do not have the same number of dimensions, prepend the shape of the smaller array with ones until both shapes have the same length.
2. Expanding single element arrays: If an array has a size of 1 in a particular dimension, it can be expanded to match the size of the other array in that dimension.
like [1,2,3,4] + 10 = [11,12,13,14] (10 is expanded to [10,10,10,10])
3. Incompatible shape, [1,2,3,4] + [1,2] -> it shows error
4.broadcasting: The arrays can be broadcast together if they are compatible in all dimensions.

'''


#problem solving using loops
prices = [100, 200, 300, 400]
discount = 10
new_prices = []
for price in prices:
    new_price = price - (price*discount/100)
    new_prices.append(new_price)
print(new_prices)

#problem solving using numpy broadcasting
import numpy as np
prices = np.array([100, 200, 300, 400])
discount = 10 #scaler single value
new_prices = prices - (prices * discount / 100)
print(new_prices)
