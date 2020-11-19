def add_pet_to_list(pet,pets = None):
    if pets is None:
        pets = []
    pets.append(pet)
    return pets
print(add_pet_to_list(''))
print(add_pet_to_list('Cow'))