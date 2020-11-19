from threading import Thread,current_thread
def display():
    print("Default Child thread name->>",current_thread().getName())
    current_thread().setName("Numpy")
    print("New child thread name->>",current_thread().getName())

print("Default Main thread name->>",current_thread().getName())
current_thread().setName("Pandas")
print("New main thread name->>",current_thread().getName())
t = Thread(target=display)
t.start()