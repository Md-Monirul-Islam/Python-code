#ylim()
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
bottom,top = plt.ylim()
print(bottom,top)   #default value printed.
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.show()