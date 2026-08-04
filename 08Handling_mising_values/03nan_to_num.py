'''
np.nan_to_num(array, nan=0.0, posinf=None, neginf=None) is a function that replaces NaN (Not a Number) values with a specified value (default is 0.0). 
It also replaces positive infinity and negative infinity with specified values if provided.
'''
import numpy as np
arr = np.array([1, 2, np.nan, 4, np.nan, 6])


#replace nan with 0
clean = np.nan_to_num(arr)
print(clean)

clean = np.nan_to_num(arr, nan=5)  # replace nan with 5
print(clean)

#replace nan with 0, posinf with 999, neginf with -999
arr = np.array([1, 2, np.inf, 4, -np.inf, 6, np.nan])
cleaned_arr = np.nan_to_num(arr, nan = 3, posinf=999, neginf=-999)  
print(cleaned_arr)
