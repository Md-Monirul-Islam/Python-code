dic1 = {"key1": 1,"key2":2,"key3":3}
dic2 = {"key1":1,"key2":4,"key3":5}
for (key,value) in set(dic1.items()) & set(dic2.items()):
    print("%s: %s is present both dic1 and dic2 " %(key,value))