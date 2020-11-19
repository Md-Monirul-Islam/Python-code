a = [1,2,3]
b = [4,5,6]
c = a+b
d = sorted(c)
d.reverse()
c[3] = 42
d.append(10)
d.extend([7,8,9])
print(c[:2])
print(d[-1])
print(len(d))

