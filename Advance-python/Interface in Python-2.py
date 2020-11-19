from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def display1(self):
        pass
    def display2(self):
        pass
class Child(Father):
    def display1(self):
        print("Child class.")
        print("display1 abstract method.")
class GandChild(Child):
    def display2(self):
        print("GrandChild class.")
        print("display2 abstract method.")
c = Child()
c.display1()
print()

g = GandChild()
g.display2()