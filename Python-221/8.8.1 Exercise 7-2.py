''''
2. Rewrite all these functions as named functions.
'''
import math
def a(x):
    return x**2
def add(x,y):
    return math.sqrt(x**2+y**2)
def c(*args):
    return sum(args)/len(args)
print(add(2,3))
