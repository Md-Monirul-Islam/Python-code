from datetime import timedelta,date
dt = timedelta(days=int(input("day number->>")))
d = date.today()
print(d)
print(d+dt)
print(d-dt)