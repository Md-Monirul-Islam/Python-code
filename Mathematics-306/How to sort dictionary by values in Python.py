import operator
dic = {1:2,2:3,3:4,4:3,2:1,0:0}
print("The origianl dictionary :",dic)
sorted_d = sorted(dic.items(),key=operator.itemgetter(0))
print("Ascending order by value :",sorted_d)
sorted_d = sorted(dic.items(),key=operator.itemgetter(0),reverse=True)
print("Desscending order by value :",sorted_d)
