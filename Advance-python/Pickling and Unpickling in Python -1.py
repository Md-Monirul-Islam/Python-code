import pickle
class Student:
    def __init__(self,name,roll,phn):
        self.name = name
        self.roll = roll
        self.phn = phn

    def display(self):
        print(f"Name : {self.name}, Roll : {self.roll}, Phone : {self.phn}")

with open("student.dat",mode="wb") as f:
    Student_1 = Student("Munna","180126","01784905235")
    pickle.dump(Student_1,f)
    print("Pickle Done!!")