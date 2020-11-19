def sub_string(str,n):
    repeat = 2
    if repeat>len(str):
        repeat=len(str)
    sub_str = str[:repeat]
    result = ''
    for i in range(n):
        result=result+sub_str
    return result
print(sub_string("mslc7",3))