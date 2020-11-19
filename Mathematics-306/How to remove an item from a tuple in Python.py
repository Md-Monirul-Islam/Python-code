tuplex = "M","A","N"
print(tuplex)
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
list1 = list(tuplex)
list1.remove("A")
tuplex = tuple(list1)
print(tuplex)