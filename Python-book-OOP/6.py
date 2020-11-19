class person:
    def _init_(self,name):
        self.name = name

    def PrintName(self):
        print(self.name)
P = person('Munna')
print(P.name)
P.PrintName()