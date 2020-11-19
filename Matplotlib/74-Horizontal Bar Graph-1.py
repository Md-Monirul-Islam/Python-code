#horisontal bar graph
import matplotlib.pyplot as plt
y = ["Science","Commerce","Arts"]
w = [100,200,300]
c = ["cyan","green","blue"]
plt.barh(y,w,[0.3,0.4,0.5],color=c,left=[20,40,50])
plt.xlabel("Courses")
plt.ylabel("Students enrolled")
plt.title("Students enrolled for the courses 2020")
plt.show()