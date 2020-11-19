import matplotlib.pyplot as plt
plt.plot([10,20,30,40],marker="*")
#plt.text(1,20,"Note",bbox={})
#plt.text(2,30,"point",bbox={"facecolor":"cyan"})
#plt.text(1,20,"note",bbox={"facecolor":"cyan","boxstyle":"circle"})
#plt.text(2,30,"point",bbox={"facecolor":"blue","boxstyle":"rarrow"})
plt.annotate("(1,20)",(1,20),(.5,25),arrowprops={},bbox={"boxstyle":"circle","pad":.9})
plt.show()