from threading import Thread
class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("Child thread.")
for i in range(5):
    print("Main mehtod.")

t = MyThread()
t.start()
t.join()