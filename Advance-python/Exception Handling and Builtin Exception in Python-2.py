a = int(input("Enter the first number->>"))
b = int(input("Enter the second number->>"))
try:
    d = a/b
    print(d)
    print("Inside try")
except ZeroDivisionError as obj:
    print(obj)
except NameError as ob:
    print(ob)
finally:
    print("Rest of the code.")