from threading import Thread
def display():
    print("Daemon Thread.")
t = Thread(target=display)
print("Before=>>",t.isDaemon())
#t.start()
t.setDaemon(True)
print("After=>>",t.isDaemon())
t.daemon = True
print("Another method to proof daemon->>",t.isDaemon())
#t.start()