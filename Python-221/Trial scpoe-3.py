myobject = ['a','b','c']
for key in ['a','b','c']:
    print(getattr(myobject, key, None))
