from threading import Thread
def display(a,b):
    print("Thread running",a,b,",Sum",a+b)
for i in range(5):
    t = Thread(target=display(10,20))
    t.start()