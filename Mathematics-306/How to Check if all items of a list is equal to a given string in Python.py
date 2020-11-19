list1 = ["White","Green","Black","Red","Orange"]
list2 = ["Green",'Green','Green','Green']
print(all(x == "Green" for x in list1))
print(all(x == "Green" for x in list2))