from threading import Thread,Condition
from time import sleep
list = []
def produce():
    cv.acquire()
    for i in range(1,6):
        list.append(i)
        sleep(1)
        print("Item produced.......")
    cv.notify()
    cv.release()

def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    sleep(2)
    print(list)

cv = Condition()
t1 = Thread(target=produce)
t2 = Thread(target=consume)
t1.start()
t2.start()
