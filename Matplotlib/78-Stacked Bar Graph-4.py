import matplotlib.pyplot as plt
boys = [100,50,110,70,60,40]
girls = [200,150,30,50,30,70]
w = 0.4
courses = ["CSE","Che","EEE","ECE","ICT","ISE"]
b = [1,2,3,4,5,6]
g = [2,3,4,5,6,7]
plt.bar(courses,boys,w,label="Boys",yerr=b)
plt.bar(courses,girls,w,bottom=boys,label="Girls",yerr=g)
plt.legend()
plt.xlabel("Courses")
plt.ylabel("Students")
plt.title("Students vs Courses")
plt.show()