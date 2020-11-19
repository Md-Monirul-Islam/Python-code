from threading import Thread
def display():
    for i in range(5):
        print("Publish video C")
t = Thread(target=display)
t.start()
for i in range(5):
    print("Publish video M")

for i in range(10):
    print("Publish video")
