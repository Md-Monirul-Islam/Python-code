''''
1. Deﬁne the following functions as lambdas, and assign them to variables:
(a) Take one parameter; return its square
(b) Take two parameters; return the square root of the sums of their squares
(c) Take any number of parameters; return their average
(d) Take a string parameter; return a string which contains
the unique letters in the input string (in any order)
'''
import math
x = int(input())
a = lambda x : x**2
b = lambda a,b : math.sqrt(a**2+b**2)
c = lambda *args: sum(args)/len(args)
d = lambda s: " ".split(set(s))

print(a)