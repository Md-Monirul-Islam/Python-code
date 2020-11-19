from threading import Thread
class MyExam:
    def solve_question(self):
        self.question_1()
        self.question_2()
        self.question_3()
    def question_1(self):
        print("Solve the question 1.")
    def question_2(self):
        print("Solve the question 2.")
    def question_3(self):
        print("Solve the question 3.")

mye = MyExam()
t = Thread(target=mye.solve_question())
print()
t1 = Thread(target=mye.question_1())
t.start()
