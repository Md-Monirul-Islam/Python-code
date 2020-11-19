#xlim()
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
#plt.xlim(1,6)  #(1)
plt.xlim(left=1,right=6)
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.show()