from threading import Thread
class MyThread:
    def display(self,a,b):
        print("Result->>",a,b)
myt = MyThread()
t = Thread(target=myt.display(10,20))
#t = Thread(target=myt.display,args=(10,20))
t.start()