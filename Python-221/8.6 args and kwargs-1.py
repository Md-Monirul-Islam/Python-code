def print_args(*args):
    for arg in args:
        print(arg)
def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print("%s: %s" % (k, v))
print(print_args('Munna','Raj','Midul'))
print(print_kwargs(name = "Monirul",age = 21,Dept = "CSE"))