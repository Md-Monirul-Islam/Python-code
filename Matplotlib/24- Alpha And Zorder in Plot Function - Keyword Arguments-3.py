import matplotlib.pyplot as plt
plt.plot([10,20,80,90],linewidth=15,zorder=2)
plt.plot([10,20,30,40],linewidth=15,zorder=1)
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.show()