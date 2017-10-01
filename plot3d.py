# 三维散点图

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 1, 1000)
z = np.random.normal(0, 1, 1000)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z)
plt.show()