from copy import deepcopy
tuplex = ("Munna",6,[],True)
print(tuplex)
tuplex_clone = deepcopy(tuplex)
tuplex_clone[2].append(50)
print(tuplex_clone)
print(tuplex)