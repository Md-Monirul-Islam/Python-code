def sum_distinct_pair(arr):
    result = 0
    i = 0
    while i<len(arr):
        result += i*arr[i] - (len(arr)-i-1)*arr[i]
        i += 1
    return result
print(sum_distinct_pair([1,2,3]))