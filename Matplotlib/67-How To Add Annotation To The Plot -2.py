import matplotlib.pyplot as plt
plt.plot([10,20,30,40],marker="*")
#plt.annotate("Note",(1,20),(.5,25),arrowprops={"color":"k","arrowstyle":"<->"})
plt.annotate("(1,20)",(0,45),annotation_clip=False)
plt.show()