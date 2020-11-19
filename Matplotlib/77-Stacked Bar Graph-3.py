import matplotlib.pyplot as plt
boys = [100,50,110,70,60,40]
girls = [200,150,30,50,30,70]
w = 0.4
courses = ["CSE","Che","EEE","ECE","ICT","ISE"]
plt.bar(courses,boys,w,label="Boys")
plt.bar(courses,girls,w,bottom=boys,label="Girls")
plt.legend()
plt.xlabel("Courses")
plt.ylabel("Students")
plt.title("Students vs Courses")
plt.show()