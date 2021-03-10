import data
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x,y,z = data.x,data.y,data.z

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z)
plt.show()
plt.savefig("../out/fig.png")

