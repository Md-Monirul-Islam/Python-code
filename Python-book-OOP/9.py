class Animal:
    def Name(self):
        pass
    def Sleep(self):
        print("Sleep")
    def MakeNoise(self):
        pass
class Dog(Animal):
    def Name(self):
        print("I have a dog.")
    def MakeNoise(self):
        print("Woof")
class Cat(Animal):
    def Name(self):
         print('My cat name is jerry.')
    def MakeNoise(self):
        print('Meow')
class Lion(Animal):
    def Name(self):
        print('Lion is the king.')
    def MakeNoise(self):
        print('Roar')
class TestAnimals:
    def PrintName(self,animal):
        animal.Name()
    def GotoSleep(self,animal):
        animal.Sleep()
    def MakeNoise(self,animal):
        animal.MakeNoise()
TestAnimals = TestAnimals()
dog = Dog()
cat = Cat()
lion = Lion()
TestAnimals.PrintName(dog)
TestAnimals.GotoSleep(dog)
TestAnimals.MakeNoise(dog)
TestAnimals.PrintName(cat)
TestAnimals.GotoSleep(cat)
TestAnimals.MakeNoise(cat)
TestAnimals.PrintName(lion)
TestAnimals.GotoSleep(lion)
TestAnimals.MakeNoise(lion)



