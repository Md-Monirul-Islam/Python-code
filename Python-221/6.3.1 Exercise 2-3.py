''''
3. Write a program which ﬁnds the factorial of a given number. E.g.
 3 factorial, or 3! is equal to 3 x 2 x 1; 5! is equal to5x4x3x2x1, etc..
  Your program should only contain a single loop.
'''
num = int(input("Please enter the number :"))
num_fac = 1
for i in range(1,num + 1):
    num_fac *= i
print("%d! = %d"%(num,num_fac))