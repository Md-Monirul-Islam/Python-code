f = open("file_1.txt",mode="w")
f.write("Growing up in the colorful life.\nMy innovation my dream.\nI love my country.")
f.close()

f = open("file_1.txt",mode="r")
data = f.read()
print(data)
f.close()
print()

f = open("file.txt",mode="r")
data_1 = f.read()
print(data_1)
f.close()

f = open("file_1.txt",mode="rb")
data_2 = f.read()
print(data_2)
f.close()