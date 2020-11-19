from threading import Thread
def display():
    for i in range(5):
        print("Child thread.")
t = Thread(target=display)
t.start()
for i in range(5):
    print("Main thread.")