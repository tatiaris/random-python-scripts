import numpy
import sys

sys.setrecursionlimit(1000000)
n = 5
nums = []

def doit(x, y):
    if x == 0:
        return y + 1
    elif y == 0 and x > 0:
        return doit(x - 1, 1)
    else:
        return doit(x - 1, doit(x, y - 1))
for i in range (n):
    print(doit(i, i))

# n = 0 ---> 1
# n = 1 ---> 3
# n = 2 ---> 7
# n = 3 ---> 61
# n = 4 ---> 340282366920938463463374607431768211453
