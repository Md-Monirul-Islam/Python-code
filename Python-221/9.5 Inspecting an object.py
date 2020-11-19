class person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def fullname(self):
        return '%s %s' %(self.name,self.surname)

obj = person('Md.Monirul Islam','Munna')
print(dir(obj))