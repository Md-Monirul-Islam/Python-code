''''
1. Write a generator function which takes an integer n as a
parameter. The function should return a generator which counts down
from n to 0. Test your function using a for loop.
'''
def my_gen(n):
    i = n
    while i >= 0:
        yield i
        i -= 1
for x in my_gen(3):
    print(x)