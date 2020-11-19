from collections import Counter
item_list = [{"item":"item1",'amount':600}, {"item":"item2","amount":500}]
result = Counter()
for d in item_list:
    result [d["item"]] += d["amount"]
print(result)
