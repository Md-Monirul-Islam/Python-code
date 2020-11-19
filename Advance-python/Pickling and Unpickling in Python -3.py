import pickle
class Student:
    def __init__(self,name,roll,result):
        self.name = name
        self.roll = roll
        self.result = result

    def display(self):
        print(f"Name->>{self.name}, Roll->>{self.roll}, Result->>{self.result}")

with open("student_1.dat",mode="wb") as f:
    stu_1 = Student("Munna","180126","5.00")
    stu_2 = Student("Monirul","180126","5.00")
    print("Pickling Done!!")
    pickle.dump(stu_1,f)
    pickle.dump(stu_2,f)

with open("student_1.dat",mode="rb") as f:
    stu_1 = pickle.load(f)
    stu_2 = pickle.load(f)
    print("Unpickling Done!!")
    stu_1.display()
    stu_2.display()