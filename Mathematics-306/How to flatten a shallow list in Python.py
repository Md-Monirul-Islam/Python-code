import itertools
original_list = [[1,2,3],[4,5,6],[8],[80,67,3]]
merged_list = list(itertools.chain(*original_list))
print(merged_list)