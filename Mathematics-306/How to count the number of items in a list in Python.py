def list_count(nums):
    count = 0
    for num in nums:
        if num==2:
            count = count+1
    return count
print(list_count([1,2,2,2,2,2,4,3,5,4]))