class person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return '%s %s' %(self.name,self.surname)
obj_1 = person('MD.Monirul Islam','Munna')
print(obj_1.fullname)