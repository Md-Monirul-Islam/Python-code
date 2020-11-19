#bar chart
import matplotlib.pyplot as plt
x = ["Science","commerce","Arts"]
h = [100,200,300]
#w = [0.1,0.2,0.3]
#b = [10,20,100]
plt.bar(x,h,bottom=10,color="green")
plt.xlabel("Couses",color="blue")
plt.ylabel("Students enrolled",color="red")
plt.title("Enrolled students for the courses")
plt.show()