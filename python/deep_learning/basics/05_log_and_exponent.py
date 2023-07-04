# log being the inverse of exponent
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10, 10, 50)
expx = np.exp(x)
logOfExpOfx = np.log(expx) 

plt.scatter(logOfExpOfx,x)
plt.show()