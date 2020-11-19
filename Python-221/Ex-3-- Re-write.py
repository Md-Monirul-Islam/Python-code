def happy_day(day):
    if day == 'Monday':
        return ":("
    if day != "Monday":
        return ":D"
print(happy_day('Sunday'))
print(happy_day('Monday'))