import matplotlib.pyplot as plt
import numpy as np
# from mpl_toolkits.mplot3d.axes3d import Axes3D

np.random.seed(42)
xs = np.random.random(100)*10+20
ys = np.random.random(100)*5+7
zs = np.random.random(100)*15+50


fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(projection='3d')
ax.scatter(xs,ys,zs)
ax.set_xlabel("This is xlabel")
ax.set_ylabel("This is ylabel")
ax.set_zlabel("This is zlabel")
ax.set_title("This is title")

# ax.view_init(elev=45,azim=55)
ax.invert_zaxis()

#change parameter: elev
for elev in [0,15,30,45,60,75,90]:
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(projection='3d')
    ax.scatter(xs,ys,zs)
    ax.set_xlabel("This is xlabel",fontsize=15)
    ax.set_ylabel("This is ylabel",fontsize=15)
    ax.set_zlabel("This is zlabel",fontsize=15)
    ax.set_title(f"This is elev={elev}",fontsize=20)
    ax.view_init(elev=elev,azim=0)

#change parameter: azim
for azim in [0,15,30,45,60,75,90]:
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(projection='3d')
    ax.scatter(xs,ys,zs,c="purple")
    ax.set_xlabel("This is xlabel",fontsize=15)
    ax.set_ylabel("This is ylabel",fontsize=15)
    ax.set_zlabel("This is zlabel",fontsize=15)
    ax.set_title(f"This is azim={azim}",fontsize=20)
    ax.view_init(elev=0,azim=azim)


#3D plot example:
labels = ["Taoyuan", "Taipei", "New Taipei"]
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(projection='3d')
for l in labels:

    ages = np.random.randint(low = 8, high = 20, size=20)

    heights = np.random.randint(130, 195, 20)

    weights = np.random.randint(30, 160, 20)

    ax.scatter(xs = heights, ys = weights, zs = ages, label=l)

ax.set_title("Age-wise body weight-height distribution")

ax.set_xlabel("Height (cm)")

ax.set_ylabel("Weight (kg)")

ax.set_zlabel("Age (years)")

ax.legend(loc="best")

plt.show()
