import datetime
today = datetime.datetime.today()
before_day = today - datetime.timedelta(days=5)
print(before_day)


#another method

from datetime import date,timedelta
dt = date.today() - timedelta(5)
print("today",today)
print("Before 5days",dt)