student_list = {"S   001":["Math","Phy"], "S   002":["Math","Che"]}
print("Original dictionary :",student_list)
student_dic = {x.translate({32:None}) : y for x,y in student_list.items()}
print("Student dictionary :",student_dic)