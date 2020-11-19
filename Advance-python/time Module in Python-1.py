from time import ctime,time,localtime
epoch = time()
print(epoch)
print(time())
print()

#current time
c_time = ctime()
print(c_time)
print(ctime())
print()

#local time
stobj = localtime()
print(stobj)
print(localtime())
print(stobj.tm_year)
print(localtime().tm_year)
print()

print("Year",stobj.tm_year)
print("Month",stobj.tm_mon)
print("Day",stobj.tm_mday)
print("Hour",stobj.tm_hour)
print("Mintue",stobj.tm_min)
print("Second",stobj.tm_sec)