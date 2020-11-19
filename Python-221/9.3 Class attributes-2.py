class person:
    pets = []
    def add_pet(self,pet):
        self.pets.append(pet)

obj_1 = person()
obj_2 = person()
obj_1.add_pet('Cat')
obj_2.add_pet("Dog")

print(obj_1.pets)
print(obj_2.pets)