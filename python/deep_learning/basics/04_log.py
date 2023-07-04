# log
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.0001, 1, 200)
# print(np.round(x,3))
logx = np.log(x)
# print(logx)
plt.plot(x,logx)
plt.show()