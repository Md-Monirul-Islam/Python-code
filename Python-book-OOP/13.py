class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print('%s is eating %s'%(self,food))
class Dog(Animal):
    def fetch(self,thing):
        print('%s goes after the %s!'%(self,thing))
class Cat(Animal):
    def swatstring(self):
        print('%s shreds the string!'%(self.name))
d = Dog('Ranger')
c = Cat('Meow')
d.fetch('ball')
c.swatstring()
d.eat('Dog food')
c.eat('Cat food')
#d.swatstring()
