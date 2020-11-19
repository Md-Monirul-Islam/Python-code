list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h','i']
print("Missing in the second list :",",".join(set(list1).difference()))
print("Aditional in the second list :",",".join(set(list2).difference()))