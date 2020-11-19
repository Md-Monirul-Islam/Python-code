''''
3. Implement a simple calculator with a menu. Display the
following options to the user, prompt for a selection, and carry
out the requested action (e.g. prompt for two numbers and add them).
each operation, return the user to the menu. Exit the program when
user selects 0. If the user enters a number which is not in the menu,
ignore the input and redisplay the menu.
You can assume that the user will enter a valid integer:
'''

Menu = """--Calculator menu--
0. Quit
1. Add two numbers
2. Subtarct two numbers
3. Multiply two numbers
4. Divide two numbers"""

selection = None
while selection != 0:
    print(Menu)
    selection = int(input("selection an option: "))

    if selection not in range(5):
        print("Invalid option: %d" %selection)
        continue
    if selection == 0:
        continue
    a = float(input("Please enter the first number: "))
    b = float(input("Please enter the second number: "))

    if selection == 1:
        result = a+b
    elif selection == 2:
        result = a-b
    elif selection == 3:
        result = a*b
    elif selection == 4:
        result = a/b
print("The result is %g " % result)


