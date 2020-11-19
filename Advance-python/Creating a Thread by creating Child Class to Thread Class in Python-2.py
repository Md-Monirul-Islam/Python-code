from threading import Thread
class MyThread(Thread):
    def run(self):
        print("Run method")
t = MyThread()
t.start()
print(t.getName())