''''
5. Rewrite the previous program so that it has two loops –
one which collects and stores the numbers, and one which processes them.
'''
numbers = []
for i in range(11):
    numbers[i] = float(input("Please enter number %d: " % (i + 1)))

total = 0
product = 1
for i in numbers:
    total += i
    product = product*i
average = total/10
print("Sum : %g\nProduct : %gAverage : %g" %(total,product,average))

