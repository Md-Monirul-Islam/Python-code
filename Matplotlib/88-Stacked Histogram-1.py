import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000,3)
plt.hist(x,30,histtype="barstacked")
plt.xlabel("Age")
plt.ylabel("Population count")
plt.title("Population age count")
plt.show()