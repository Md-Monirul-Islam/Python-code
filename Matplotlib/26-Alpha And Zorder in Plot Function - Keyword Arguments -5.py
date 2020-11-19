import matplotlib.pyplot as plt
plt.plot([0,0],[-1,1],linewidth=15,zorder=3)
plt.plot([-1,1],[-1,1],linewidth=15,zorder=2)
plt.plot([-1,1],[1,-1],linewidth=15,zorder=1)
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.show()