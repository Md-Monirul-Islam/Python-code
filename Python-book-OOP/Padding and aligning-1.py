print("{:12}".format('Python'))

print("{:>15}".format("Python"))

print("{:<15}".format("Python"))

print(len("{:*<15}".format("Python")))

print("{:#>15}".format("Python"))

print("{:*^12}".format("Python"))

print("{:.15}".format("Python object oriented programming"))

print("{:.{}}".format("Python object oriented programming",15))

#Named placeholders

data = {'Name':'Munna','Place':'Pabna','Address':'AK road Pabna'}

print('{Name} {Place} {Address}'.format(**data))

from datetime import datetime

print('{:%y/%m/%d.%H:%M}'.format(datetime(2018,3,12,9,56)))