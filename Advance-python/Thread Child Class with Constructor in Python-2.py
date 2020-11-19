from threading import Thread
class MyThread(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        print("Child thread constructor.",a)
    def run(self):
        pass
        #print("Child thread")
print("Main thread")

t = MyThread(10)
t.start()