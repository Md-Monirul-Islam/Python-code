from threading import Thread
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Child thread constructor.")
    def run(self):
        pass
        #print("Child thread")
print("Main thread")

t = MyThread()
t.start()