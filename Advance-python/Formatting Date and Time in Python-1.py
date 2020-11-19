from datetime import datetime
dt = datetime.today()
print(dt)
print(type(dt))
print()

newd1 = dt.strftime("%B,%d,%Y")
print(newd1)
print()

newd2 = dt.strftime("%d/%b/%Y")
print(newd2)
print()

newd3 = dt.strftime("%d-%m-%Y")
print(newd3)
print()

new1 = dt.strftime("%H:%M:%S")
print(new1)
print(type(new1))
print()

print(help(datetime))