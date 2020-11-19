from abc import ABC,abstractmethod
class DefenceForce:
    @abstractmethod
    def area(self):
        pass
    def gun(self):  #concreate method.
        print("Gun->>AK47")
class Army(DefenceForce):
    def area(self):
        print("Army area->>Land")
class AirForce(DefenceForce):
    def area(self):
        print("AirForce area->>Sky")
class Navy(DefenceForce):
    def area(self):
        print("Navy area->>Sea")
a = Army()
af = AirForce()
n = Navy()

a.area()
a.gun()
print()

af.area()
af.gun()
print()

n.area()
n.gun()
