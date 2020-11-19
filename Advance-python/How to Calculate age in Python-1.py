from datetime import date
date_of_birth = date(1998,2,2)
today = date.today()
age = today.year - date_of_birth.year - ((today.month,today.day) < (today.month,today.day))
print(age)
print(2-False)
print(2-True)