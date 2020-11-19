dic =  {"c1":[1,2,3],"c2":[4,5,6],"c3":[7,8,9]}
for row in zip(*([key] + (value) for key ,value in sorted(dic.items()))):
    print(*row)