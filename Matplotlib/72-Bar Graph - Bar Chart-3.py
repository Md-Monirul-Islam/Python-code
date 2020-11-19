#bar chart
import matplotlib.pyplot as plt
x = ["Science","Commerce","Arts"]
h = [100,200,300]
c = ["red","green","cyan"]
plt.bar(x,h,align="edge",color=c,edgecolor="k",linewidth=10)
plt.xlabel("Course")
plt.ylabel("Students enrolled")
plt.title("Enrolled students for the courses")
plt.show()