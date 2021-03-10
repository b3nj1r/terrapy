import data
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# collect data
x,y,z = data.x,data.y,data.z

# setup and plot data
fig,ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.scatter(x,y,z)

# show visual
plt.savefig("../out/fig.png")
plt.show()

