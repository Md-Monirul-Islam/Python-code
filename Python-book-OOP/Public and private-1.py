class Vehical:

    def __init__(self,name):
        self.name = name
        self._name = name
        self.__name = name
    def var(self):
        print("the main value")


a = Vehical('bus')
print(a.name)
print(a._name)
print(a._Vehical__name)
a.var()

