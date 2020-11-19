from threading import Thread
def display(a,b):
    print("Thread running",a,b)
t = Thread(target=display(10,20))
t.start()