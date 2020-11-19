import datetime
base = datetime.datetime.today()
for x in range(1,6):
    print(base + datetime.timedelta(days=x))