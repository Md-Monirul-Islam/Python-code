l = [{"V":"S001"},{"V":"S002"},{"V":"S009"},{"VIII":"S007"}]
print("Original list :",l)
u_value = set(val for dic in l for val in dic.values())
print("Unique value :",u_value)
