''''
1. . Write a program which repeatedly prompts the user
for an integer. If the integer is even, print the integer. If the integer is odd,
don’t print anything. Exit the program if the user enters the integer 99.
'''
for num in range(1,100):
    if num == 99:
        break
    if num%2== 0:
        continue
    print(num)