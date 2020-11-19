def concatenate(list):
    result = ''
    for element in list:
        result += str(element)
    return result
print(concatenate(["Munna",1,2,3,4]))