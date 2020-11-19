dic = [{"key": {"sub_key":1}},{"key": {"sub_key":10}}]
print("Main dictionary :",dic)
dic.sort(key=lambda x:x["key"]["sub_key"],reverse=True)
print("Sorted dictionary :",dic)