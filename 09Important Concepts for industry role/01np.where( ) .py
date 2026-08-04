'''
- np.where() → Creates a new array based on condition.
- np.where() is a conditional function in NumPy that works like an if-else statement for arrays.
It lets you replace values, select elements, or find indices based on a condition.

    np.where(condition, value_if_true, value_if_false)

    condition → Boolean expression (e.g., arr > 30)
    value_if_true → Returned when condition is True
    value_if_false → Returned when condition is False

'''
import numpy as np

#Basic If-Else
arr = np.array([10, 20, 30, 40, 50])
result = np.where(arr > 30, "High", "Low")
print(result)

#Find Indices Only
#If you pass only the condition:
#This returns the indices where the condition is True.
arr = np.array([10, 20, 30, 40, 50])
index = np.where(arr > 30)
print(index[0])   # [3 4]
print(arr[index]) # [40 50]


#Replace Negative Numbers
arr = np.array([-5, 3, -2, 8, 1])
new = np.where(arr < 0, 0, arr)
print(new)

#Multiple Conditions (Nested)
marks = np.array([35, 60, 85, 45])

grade = np.where(
    marks >= 75,
    "A",
    np.where(marks >= 50, "B", "C")
)

print(grade)


#Real Industry Example
#Suppose a company gives a 10% discount to products priced above ₹1000.

price = np.array([500, 1500, 900, 2500])

final_price = np.where(
    price > 1000,
    price * 0.90,
    price
)

print(final_price)
