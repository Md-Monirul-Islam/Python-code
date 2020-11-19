f = open("file.txt",mode='w')
list = ["Green"," Red"," Blue"," Yellow"]
f.writelines(list)
f.close()
print("SUCCESS.")