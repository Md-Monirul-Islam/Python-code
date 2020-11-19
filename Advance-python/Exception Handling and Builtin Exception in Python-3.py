a = int(input("Enter the first number->>"))
b = int(input("Enter the second number->>"))
try:
    d = a/b
    print(d)
    print("Inside try")
except (ZeroDivisionError,NameError) as obj:
    print(obj)

finally:
    print("Rest of the code.")