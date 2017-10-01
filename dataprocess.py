import pandas as pd
all_the_dots = []
data = pd.read_excel("data.xlsx")
for i in data['dot']:
    for each_dot in eval(i):
        all_the_dots.append(each_dot)
# print(all_the_dots)
while (0.0, 0.0, 0.0) in all_the_dots:

    all_the_dots.remove((0.0, 0.0, 0.0))
# print((0.0, 0.0, 0.0) in all_the_dots)
# 删除所有的零点元素
xs = [i[0] for i in all_the_dots]
ys = [i[1] for i in all_the_dots]
zs = [i[2] for i in all_the_dots]
hot = [1/(i[0]**3 + i[1]**3 + i[2]**3) for i in all_the_dots]   # 计算值
print(max(hot))
print(min(hot))
# 三维点坐标
# 颜色使用公式 笛卡尔立方分之一
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random as ran

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cmhot = plt.cm.get_cmap("hot")
xs = xs
ys = ys
zs = zs
l = ax.scatter(xs, ys, zs, c=hot, cmap=cmhot)
fig.colorbar(l)
plt.show()