def add_pet_to_list(pet,pets=[]):
    pets.append(pet)
    return pets
print(add_pet_to_list("Cat"))
list_with_dog = add_pet_to_list("dog")
print(list_with_dog)