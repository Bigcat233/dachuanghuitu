import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random as ran

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cmhot = plt.cm.get_cmap("hot")
xs =  [ran.random()*50 for n in range(0,50)]
ys = [ran.random()*50 for n in range(0,50)]
zs = [ran.random() for n in range(0,50)]
l = ax.scatter(xs, ys, zs, c=zs, cmap=cmhot)
fig.colorbar(l)
plt.show()