#bar chart
import matplotlib.pyplot as plt
a = ["CSE","ISE","ICT","EEE","Che","Mech","Tex"]
h = [250,230,200,250,220,230,200]
c = ["cyan","blue","yellow","green","red","yellow","k"]
plt.bar(a,h,color=c,width=0.3)
plt.xlabel("Engineering courses")
plt.ylabel("Students enrolled")
plt.title("Enrolled Engineering students for the courses")
plt.show()