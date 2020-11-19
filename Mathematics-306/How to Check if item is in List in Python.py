def is_group_data(group_data,n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_data([1,2,3,4,5,6],4))