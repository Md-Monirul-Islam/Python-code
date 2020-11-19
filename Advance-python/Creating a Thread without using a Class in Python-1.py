from threading import Thread
def display():
    print("Thread running.")
t = Thread(target=display)
t.start() 