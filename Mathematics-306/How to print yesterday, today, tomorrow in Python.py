import datetime
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Today :",today)
print("Yesterday :",yesterday)
print("Tomorrow :",tomorrow)