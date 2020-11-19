''''
1. Rewrite the hypotenuse function from exercise 2 so that it returns a value instead of printing it.
Add exception handling so that the function returns
None if it is called with parameters of the wrong type.
'''
import math
def hypotenuse(x,y):
    try:
        return math.sqrt(x**2 + y**2)
    except TypeError:
        return None
print(hypotenuse(10,12))
print(hypotenuse('2','5'))
print(hypotenuse(2,'4'))