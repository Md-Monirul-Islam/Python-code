def make_greeting(title,name,surname,formal=True):
    if formal:
        return "Hello, %s %s!" %(title,surname)
    return "Hello, %s"%name
print(make_greeting("MD.","Monirul Islam","Munna"))
print(make_greeting("MD.","Monirul Islam","Munna",False))