#bar chart
import matplotlib.pyplot as plt
x = ["Science","commerce","Arts"]
h = [200,300,500]
plt.bar(x,h,color="cyan",width=0.2)  #width by default is 0.8
plt.xlabel("Courses")
plt.ylabel("Students enrolled")
plt.title("Enrolled students for the courses")
plt.show()