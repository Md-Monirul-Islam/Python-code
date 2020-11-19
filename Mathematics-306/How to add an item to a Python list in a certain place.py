subject_list = ["Physics",'Math','Chemistry']
print("Real subject :",subject_list)
subject_list = [x for elmnt in subject_list for x in ("B",elmnt)]
print("Real subject :",subject_list)