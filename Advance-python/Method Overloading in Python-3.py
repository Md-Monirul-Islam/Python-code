class MyClass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = "Provide at least two numbers."
        return s
object = MyClass()
print(object.sum(10,20,30))
print(object.sum(10,20))