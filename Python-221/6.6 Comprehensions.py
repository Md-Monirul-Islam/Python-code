numbers = [1,5,2,12,14,7,18]
double = []
for number in numbers:
    double.append(2*number)

print(double)

even_num = []
for number in numbers:
    if number%2==0:
        even_num.append(number)
print(even_num)

animals = ['aardvark', 'cat', 'dog', 'opossum']
vowel_animals = []
for animal in animals:
    if animal[0] in "aeiou":
     vowel_animals.append(animal.title())

print(vowel_animals)