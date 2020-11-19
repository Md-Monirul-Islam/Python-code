import os
if os.path.isfile("file_2.txt"):
    f = open("file_2.txt")
    print("File opend.")
    f.close()
else:
    print("File is not found.")