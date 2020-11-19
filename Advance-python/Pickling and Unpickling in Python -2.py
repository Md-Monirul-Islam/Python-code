import pickle
class Student:
    def __init__(self,name,roll,phn):
        self.name = name
        self.roll = roll
        self.phn = phn

    def display(self):
        print(f"Name->>{self.name}, Roll->>{self.roll}, Phone->>{self.phn}")

with open("student.dat",mode="rb") as f:
    student_1 = pickle.load(f)
    print("Unpickle Done!!!")
    student_1.display()