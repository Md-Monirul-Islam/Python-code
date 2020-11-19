def dic_depth(d):
    if isinstance(d,dict):
        return 1 + (max(map(dic_depth,d.values())) if d else 0)
    return 0
dic = {'a':1,"b":{"c": {"d": {}}}}
print(dic_depth(dic))

