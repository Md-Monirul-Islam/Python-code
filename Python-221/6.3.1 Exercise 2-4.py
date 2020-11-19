''''
4. Write a program which prompts the user for 10 ﬂoating-point numbers and calculates their sum,
product and average. Your program should only contain a single loop.
'''
total = 0
product = 1
for i in range(1,10+1):
    num = float(input("Please enter the floating point number %d :" %i))
    total += i
    product *= i
average = total/10
print("Sum : %g\nProduct : %g\nAverage : %g" %(total,product,average))