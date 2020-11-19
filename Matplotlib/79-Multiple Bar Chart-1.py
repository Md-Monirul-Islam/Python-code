import matplotlib.pyplot as plt
import numpy as np
courses = ["CSE","ICE","EEE","ISE","CHEM"]
boys = [200,120,170,80,75]
girls = [150,90,60,90,100]
w = 0.4
bar_1 = np.arange(len(courses))
bar_2 = [i+w for i in bar_1]
plt.bar(bar_1,boys,w,label="Boys")
plt.bar(bar_2,girls,w,label="Girls")
plt.legend()
plt.xticks(bar_1+w/2,courses)
plt.xlabel("Courses")
plt.ylabel("Students")
plt.title("Students vs Courses")
plt.show()