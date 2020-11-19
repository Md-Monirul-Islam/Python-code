import itertools
num = [[10,20],[40],[30,56,25],[10,20],[33],[40]]
print("Original list :",num)
num.sort()
new_list = list(num for num,_ in itertools.groupby(num))
print("New List :",new_list)