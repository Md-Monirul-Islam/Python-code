class Student:
    #constructor
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    #instance method
    def display(self):
        print("The student name is",self.name)
        print("The student roll number is",self.roll)
class User:
    #static method
    @staticmethod
    def show(details):
        print("The student name is",details.name)
        print("The student name is",details.roll)

#creating object of Student class

stu = Student("MD.Monirul Islam",180126)
User.show(stu)
