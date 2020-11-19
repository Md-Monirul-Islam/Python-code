import matplotlib.pyplot as plt
import numpy as np
w = 0.2
countries = ["Bangladesh","pakistan","Russia","Nepal","japan"]
gold = [10,12,6,9,13]
silver = [50,60,35,45,75]
bronze = [100,90,110,70,80]
bar_1 = np.arange(len(countries))
bar_2 = [i+w for i in bar_1]
bar_3 = [j+w for j in bar_2]
plt.bar(bar_1,gold,w,label="Gold")
plt.bar(bar_2,silver,w,label="Silver")
plt.bar(bar_3,bronze,w,label="Bronze")
plt.xlabel("Countries")
plt.ylabel("Medals")
plt.title("Countries vs Medals")
plt.xticks(bar_1+w,countries)
plt.legend()
plt.show()