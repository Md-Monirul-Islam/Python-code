from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def display(self):
        pass
class Child(Father):
    def display(self):
        print("Child class.")
        print("Defining abstract method.")
c = Child()
c.display()