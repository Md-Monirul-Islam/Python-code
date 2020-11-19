def make_greeting(title,name,surname,formal=True,time=None):
    if formal:
        fullname = "%s %s" %(title,surname)
    else:
        fullname = name
    if time is None:
        greeting = "Hello!"
    else:
        greeting = "Good %s" %time
    return "%s, %s" %(greeting,fullname)
print(make_greeting("MD.","Monirul Islam","Munna"))
print(make_greeting("MD.","Monirul Islam","Munna",False))
print(make_greeting("MD.","Monirul Islam","Munna",False,"Night"))
print(make_greeting(title="MD.", name="Monirul Islam", surname="Munna"))