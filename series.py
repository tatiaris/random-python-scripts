import math
import numpy as np
import matplotlib.pyplot as plt

limit = 10000000                                                # sets the number of elements to be added
sum = 0                                                         # sets the sum to 0 when program is restarted
xList = []                                                      
yList = []
def logSum(n):
    global sum
    global xList
    global yList
    while n <= limit:                                           # while loop that runs 'limit' number of times
        sum += 1/n                                              # adds 1/n to the sum
        power = round(math.log(n, 10), 9)
        if n > 9 and power % math.floor(power) == 0:
            xList.append(n)
            yList.append(sum)
        n += 1                                                  # increment n by 1
logSum(1)                                                       # run the function
print("Sum = " + str(sum))                                      # print the final sum
plt.scatter(xList, yList)
print(xList)
print(yList)
