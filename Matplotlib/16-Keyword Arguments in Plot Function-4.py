import matplotlib.pyplot as plt
plt.plot([10,20,30,40],color="red",dashes=[2,6])#2=length,3=space
plt.plot([12,9,32,42],c="k",dashes=[3,9])
plt.plot([5,6,7,8],color="c",dashes=[3,8])
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("first plot")
plt.show()