class Student:
    def __init__(self,name,roll,result):
        self.name = name
        self.roll = roll
        self.result = result

    def display(self):
        print(f"Name->>{self.name}, Roll->>{self.roll}, Result->>{self.result}")