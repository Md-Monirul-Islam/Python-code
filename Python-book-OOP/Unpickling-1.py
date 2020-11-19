import pickle

class Animal:
    def __init__(self,number_of_legs,color):
        self.number_of_legs = number_of_legs
        self.color = color

class Cat(Animal):
    def __init__(self,color):
        Animal.__init__(self,4,color)

pussy = Cat('White')

my_pickle_pussy = pickle.dumps(pussy)
Meow = pickle.loads(my_pickle_pussy)
Meow.color = 'black'

print(str.format('meow is {0}',Meow.color))

print(str.format('pussy is {0}',pussy.color))
