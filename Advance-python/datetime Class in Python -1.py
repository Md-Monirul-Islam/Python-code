from datetime import datetime
dt1 = datetime(year = 2020, month=6, day=30)
dt2 = datetime(year=2020,month=6,day=30,hour=15,minute=30)
dt3 = datetime(2020,9,15)
dt4 = datetime(2020,9,15,10,10)
print(dt1)
print()
print(dt2)
print()
print(dt3)
print()
print(dt4)
print()

print(dt1.year)
print()
print(dt4.minute)
print()


#current date time
current_datetmie = datetime.now()
print(current_datetmie)
print(current_datetmie.hour)
print(current_datetmie.minute)
print(current_datetmie.month)