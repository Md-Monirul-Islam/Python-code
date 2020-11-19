value_dic = {'value1':4040,"value2":3794,"value3":3456,"value4":2354,"value5":1234}
value_max = max(value_dic.keys(),key=(lambda k: value_dic[k]))
value_min = min(value_dic.keys(),key=(lambda k: value_dic[k]))
print("Maximum value :",value_max)
print("Minimum value :",value_min)