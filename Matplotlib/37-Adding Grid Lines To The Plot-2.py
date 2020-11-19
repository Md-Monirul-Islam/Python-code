import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[5,6,7,8])
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.minorticks_on()
plt.grid(b=True,which="minor",color="blue")  #by default major.
plt.grid(b=True,color="red",linewidth=20)
plt.show()
print(help(plt.grid))