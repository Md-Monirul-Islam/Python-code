import matplotlib.pyplot as plt
x = ["Bangladesh","Katar","Pakistan","Iran","iraque","Mishar"]
gold = [15,8,23,12,7,9]
silver = [40,30,60,80,75,35]
bronze = [100,90,60,150,175,130]
plt.bar(x,gold,width=0.4,label="Gold")
plt.bar(x,silver,width=0.4,bottom=gold,color="cyan",label="Silver")
plt.bar(x,bronze,width=0.4,bottom=silver,label="Bronze")
plt.legend(loc="upper left")
plt.xlabel("Countries")
plt.ylabel("Medals")
plt.title("Countries vs Medals")
plt.show()