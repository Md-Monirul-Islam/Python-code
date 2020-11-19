from threading import Thread,current_thread
def display():
    pass
t = Thread(target=display)
print("Defaul name->>",t.getName())
t.setName("Numpy")
print("New name->>",t.getName())
t.start()