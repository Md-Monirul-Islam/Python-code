class person:
    TITLES = ('Mr','Dr','Ms','Mrs')
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def fullname(self):
        return '%s %s' %(self.name,self.surname)

    @classmethod
    def allowed_title_starting_with(cls,startswith):
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def allowed_tile_ending_with(endswith):
        return [t for t in person.TITLES if t.endswith(endswith)]

obj1 = person('Md.Monirul Islam','Munna')

print(obj1.fullname())

print(obj1.allowed_title_starting_with('M'))
print(person.allowed_title_starting_with('M'))

print(obj1.allowed_tile_ending_with('s'))
print(person.allowed_tile_ending_with('s'))