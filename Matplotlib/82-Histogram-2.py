import matplotlib.pyplot as plt
x = [12,34,70,23,67,90,56,75,33,56,
     23,77,45,78,45,8,
     32,100,70,32,23,
     90,67,45,50,75,79,
     54,21,28,54,89,67,45
    ,67,38,60,46,65,20,91,60,57]
y = [1,11,21,31,41,51,61,71,81,91,101]
plt.hist(x,y,edgecolor="red")
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Population age count")
plt.xticks(y)
plt.show()