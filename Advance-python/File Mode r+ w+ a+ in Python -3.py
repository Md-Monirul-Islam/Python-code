f = open("file_1.txt",mode="a+")
print(f.tell())
f.write("infinix zero 8")
f.seek(22)
print(f.tell())
data = f.read()
print(f.tell())
print(data)
f.close()