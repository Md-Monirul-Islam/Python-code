import matplotlib.pyplot as plt
plt.plot([10,20,30,40],marker="*")
ax = plt.gca()
plt.text(0.5,0.5,"NOTE",transform=ax.transAxes,color="red",size=15)
print(plt.ylim())
print(plt.text(0,0,"NOTE"))
plt.show()