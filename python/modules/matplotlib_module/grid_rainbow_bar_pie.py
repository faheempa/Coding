import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([0, 5, 25, 15, 30])

# # 1 - grid
# plt.grid(color="red", linewidth=1, linestyle="--")
# plt.plot(a,b)

# # 2 - selecting axis
# plt.grid(axis="y",color="red", linewidth=1, linestyle="--")
# plt.plot(a,b)

# 3 - picking different colors
# colors=["red", "blue", "orange", "green", "black"]
# plt.scatter(a,b, c=colors)

# 4 - using rainbow colors
# color_positions=np.array([2,5,7,3,9])
# plt.scatter(a,b,cmap="rainbow", c=color_positions)
# plt.colorbar()
# plt.grid()

# 5 - bar chart
# toys = ["car", "doll", "truck", "plane"]
# stock=[5,8,3,4]
# colors=["red", "blue", "yellow", "green"]
# # vertical
# plt.bar(toys, stock, color=colors, width=0.5)
# # horizontal
# plt.barh(toys, stock, color=colors)
# plt.title("stock of toys")
# plt.xlabel("toys")
# plt.ylabel("stock")

# 6 - pie chart
# toys = ["car", "doll", "truck", "plane"]
# stock=[5,8,3,4]
# colors=["red", "blue", "yellow", "green"]
# plt.pie(stock, labels=toys, startangle=90, colors=colors, shadow=True)

# 7 - sectioning out the pie chart and adding a legend
toys = ["car", "doll", "truck", "plane"]
stock = [5, 8, 3, 4]
colors = ["red", "blue", "yellow", "green"]
section_out = [0, 0.1, 0.3, 0.2]
plt.pie(
    stock, labels=toys, startangle=90, colors=colors, shadow=True, explode=section_out
)
plt.legend(loc="upper left", bbox_to_anchor=(1,1))



plt.show()
