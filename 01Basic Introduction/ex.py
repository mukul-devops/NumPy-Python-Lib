#it's for a example of numpy use
tempreature = [34,65,45,23,65]
total = 0
for temp in tempreature:
    total+= temp
avg = total/len(tempreature)
print(avg)

#same concept using numpy 
import numpy as np

tempreature = np.array([34,65,45,23,65])
average = np.mean(tempreature)
print(average)



