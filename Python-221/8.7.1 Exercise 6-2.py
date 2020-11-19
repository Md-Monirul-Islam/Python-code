''''
2. Test the decorator by applying it to a function which takes two
 arguments and returns their sum. Print the result
of the function, and what was logged to the ﬁle.
'''
@log
def add(x,y):
    return x+y
print(add(3,5))
with open("log.txt", "r") as logfile:
    print(logfile.read())
