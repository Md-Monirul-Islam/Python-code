nums = [1,2,3,-5,4,6,-6]
print("Original number in the list :",nums)
new_nums_list = list(filter(lambda x : x > 0,nums))
print(new_nums_list)