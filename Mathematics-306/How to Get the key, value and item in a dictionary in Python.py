dic = {1:10,2:20,3:30,4:40,5:50,6:60,7:70,8:80}
print("Key    Value    Count")
for count, (key,value) in enumerate(dic.items(),1):
    print(key,"     ",value,"     ",count)