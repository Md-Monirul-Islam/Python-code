from threading import current_thread,Thread
def display():
    print("Child thread name->>",current_thread().getName())
t_1 = Thread(target=display)
t_2 = Thread(target=display)
t_1.start()
t_2.start()
print("Main thread name->>",current_thread().getName())