def multiplie(items):
    total = 1
    for x in items:
        total *= x
    return total

print(multiplie([1,2,3,-3]))