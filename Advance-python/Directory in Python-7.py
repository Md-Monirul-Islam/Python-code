import os
w = os.walk("yourdir",topdown=False)
for i in w:
    print(i)