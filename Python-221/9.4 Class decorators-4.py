class person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return '%s %s' %(self.name,self.surname)

    @fullname.setter
    def fullname(self,value):
        name, surname = value.split(' ',1)
        self.name = name
        self.surname = surname

    @fullname.deleter
    def fullname(self):
        del self.name
        del self.surname

obj1 = person('MD.Monirul Islam','Munna')
print(obj1.fullname)

obj1.fullname = 'Jovial Munna'
print(obj1.fullname)
print(obj1.name)
print(obj1.surname)