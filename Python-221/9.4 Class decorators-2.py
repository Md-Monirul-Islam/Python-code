class person:
    def __init__(self,height):
        self.height = height

    def get_height(self):
        return self.height

    def set_height(self,height):
       self.height = height

Munna = person(150)
Munna.height += 1
print(Munna.set_height(Munna.height+1))