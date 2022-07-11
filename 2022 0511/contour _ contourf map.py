import numpy as np
import matplotlib.pyplot as plt

t1=np.arange(4)
t2=np.arange(4)
T1,T2=np.meshgrid(t1,t2)

fig,ax=plt.subplots(figsize=(7,7))
ax.scatter(T1,T2,c="red")

def f(x,y):
    return np.exp(-x**2)*np.exp(y)

x = np.linspace(-2,2,200)
y = np.linspace(-2,2,200)
X,Y = np.meshgrid(x, y)

# initial map
fig,ax=plt.subplots(figsize=(7,7))
ax.contourf(x,y,f(X,Y),cmap='coolwarm',levels=10)
axes=ax.contour(x,y,f(X,Y),colors="black",levels=10)
plt.clabel(axes, inline=True, fontsize=10)

# imporve map
cf_lv = [0,0.05,0.3,1,2,4,6,np.exp(2)]
line_lv = [0.05,0.3,1,2,4,6]
lb_pos = [(0,1.8),(0,1.4),(0,0.8),(-0.75,0.7),(0.75,0.7),\
            (-1,0),(1,0),(-1.5,-1),(1.5,-1)]
fig,ax=plt.subplots(figsize=(7,7))
axes=ax.contourf(x,y,f(X,Y),cmap='coolwarm',levels=cf_lv,alpha=0.75)
# axes=ax.contourf(x,y,f(X,Y),cmap='coolwarm_r',levels=cf_lv,alpha=0.75)
axes_l=ax.contour(x,y,f(X,Y),colors="black",levels=line_lv)
ax.clabel(axes_l, inline=True, fontsize=10,manual=lb_pos)
ax.set_ylabel("Y")
ax.set_xlabel("X")
ax.set_title("example 1")
fig.colorbar(axes)
# cbar = fig.colorbar(axes,  ticks=[0, 1.5, 6], orientation='horizontal')
# cbar.ax.set_xticklabels(['low', 'medium', 'high'])