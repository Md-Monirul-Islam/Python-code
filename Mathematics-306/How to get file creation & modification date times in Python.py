import os.path,time
print(time.ctime(os.path.getatime("abc.txt")))
print(time.ctime(os.path.getctime("ad.txt")))