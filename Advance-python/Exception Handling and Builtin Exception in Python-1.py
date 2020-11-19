a = int(input("Enter the first number->>"))
b = int(input("Enter the second number->>"))
try:
    d = a/b
    print(d)
    print("inside try.")
except ZeroDivisionError:
    print("Divison by zero not Allowed")
else:
    print("Else side.")
finally:
    print("Must be printed.")
print("Rest of the code.")