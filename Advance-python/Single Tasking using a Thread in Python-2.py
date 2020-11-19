from threading import Thread
from time import sleep
class MyExam:
    def solve_question(self):
        self.question_1()
        self.question_2()
        self.question_3()

    def question_1(self):
        print("Solve the question 1.")
        sleep(3)
    def question_2(self):
         print("Solve the question 2.")
         sleep(3)
    def question_3(self):
        print("Solve the question 3.")
        sleep(3)

mye = MyExam()
t = Thread(target=mye.solve_question())
t.start()