import matplotlib.pyplot as plt
import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([0, 5, 25, 15, 30])
c =np.array([1,23,34,51,70])
d =np.array([50,70,90,100,110])

# 1 - basic ploting
# plt.plot(a,b)

# 2 - defualt x axis
# plt.plot(a)


# 3 - plotting multiple graphs together
# plt.plot(a,b, c="red")
# plt.plot(c,d, c="blue")
# plt.plot(a,d, c="yellow")

# 4
# plt.plot(a,b,marker="o") # point
# plt.plot(a,b,marker="*") # star
# plt.plot(a,b,marker="d") # diamond
# plt.plot(a,b,marker="x") # cross
# plt.plot(a,b,marker="<") # <| like triangle
# plt.plot(a,b,marker="s") # square

# 5
# plt.plot(a,b,marker = "o", c="blue", ls="-", ms=5, mfc="black", mec="black", lw=2)
# c - color
# ls - line style
# ms - marker size
# mfc - marker face color
# mec - maker edge color
# lw - line width

# 6
# show only points
# plt.scatter(a,b)

# 7 - title, labels and legends
font1=dict(family="serif", size=25, color="red")
plt.title("Graph 1", font1)
plt.xlabel("Time(s)", font1)
plt.ylabel("Distance(m)", fontdict=font1)
plt.plot(a,b, label="first")
plt.plot(c,d, label="second")
plt.legend()



plt.show()