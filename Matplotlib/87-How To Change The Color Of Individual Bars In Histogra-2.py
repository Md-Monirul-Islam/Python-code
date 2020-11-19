import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
n,m,patches = plt.hist(x,bins=10,align="right")
print(n)
color = ["blue","orange","cyan","red","green","yellow","#FFFF00","#00FF00",
         "#CCCC00","black"]
for i in range(len(n)):
    c = color[i]
    patches[i].set_facecolor(c)
plt.xlabel("Age")
plt.ylabel("people count")
plt.title("Age graph")
plt.show()
