from threading import Thread,Event
from time import sleep

def light_switch():
    sleep(3)
    e.set()
    print("Green light on.\n")
    sleep(5)
    print("Red light on.")
    e.clear()

def traffic():
    e.wait()
    while e.is_set():
        print("You can go->>>>>>>>")
        sleep(.5)
    print("Maintain traffic jam")

e = Event()
t1 = Thread(target=light_switch)
t2 = Thread(target=traffic)
t1.start()
t2.start()
t1.join()
t2.join()