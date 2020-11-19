def print_everything(*args,**kwargs):
    for arg in args:
        print(arg)

    for k, v in kwargs.items():
        print("%s, %s" %(k,v))

# we can write all the parameters individually
print_everything("Cat","Dog",day='Friday')

t = ("Cat",'Dog')
d = {'day':'Friday'}

# we can unpack a tuple and a dictionary

print_everything(*t,**d)

# or just one of them
print_everything(*t,day='Friday')
print_everything('Cat','Dog',**d)

# we can mix * and ** with explicit parameters
print_everything('Cat',*t,**d)

# none of these are allowed:
print_everything(*t, "Jane", **d)
print_everything(*t, **d, time="evening")