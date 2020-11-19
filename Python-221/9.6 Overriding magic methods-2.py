class person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def __ge__(self, other):
        if self.surname == other.surname:
            return self.name > other.surname
        return self.surname > other.surname

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return not self > other

    def __lt__(self, other):
        return not (self > other or self == other)

    def _ge_(self,other):
        return not self < other

#Munna = person('Munna','Islam')
#print(Munna)