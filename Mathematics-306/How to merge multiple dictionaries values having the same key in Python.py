from collections import Counter
dic1 = {'a':100,"b":300,"c":500}
dic2 = {'a':400,'b':500,'d':300}
new_dic = Counter(dic1) + Counter(dic2)
print(new_dic)