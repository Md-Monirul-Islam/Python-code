from threading import Thread,current_thread
def display():
    print("display function.")
mt = current_thread()
print(mt.getName())
print("mt->>",mt.isDaemon())
t1 = Thread(target=display)
print("t1 Before->>",t1.isDaemon())
t1.setDaemon(True)
print("t1 After->>",t1.isDaemon())
t1.start()