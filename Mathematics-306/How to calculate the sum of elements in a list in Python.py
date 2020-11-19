num = int(input("How many numbers : ?"))
list = []
for n in range(num):
    numbers = int(input("Enter the number :"))
    list.append(numbers)
print("Sum of them is : ",sum(list))