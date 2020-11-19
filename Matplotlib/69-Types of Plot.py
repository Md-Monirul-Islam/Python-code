#line graph
import matplotlib.pyplot as plt
year = [1920,1930,1940,1950,1960,1970,1980,1990,2000]
emplye = [12,25.45,67,37.3,22.33,11,21.12,42.23,15.23]
plt.plot(year,emplye,marker="o",linestyle="-.",color="cyan")
plt.xlabel("year")
plt.ylabel("emplye")
plt.title("rate of emplye")
plt.show()