from datetime import date
d1 = date(year=2020,month=9,day=16)
d2 = date(year=2019,month=9,day=16)
d3 = date(2020,9,16)
print(d1)
print(d3)
print(d1.__sub__(d2))
print(d1-d2)
print(d1.year)
print(d2.month)
print(d3.day)
print()

#use today()
cd = date.today()
print(cd)
print(cd.year)