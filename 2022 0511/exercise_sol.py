import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel("data.xlsx")

def plane_regression_order3(data):
    n=len(data)
    X=np.ones((n,10))
    D=np.ones((n,1))
    for i in range(n):
        D[i]=data["d"][i]
        X[i][1]=data["x"][i]
        X[i][2]=data["y"][i]
        X[i][3]=(data["x"][i])**2
        X[i][4]=(data["y"][i])**2
        X[i][5]=(data["x"][i])*data["y"][i]
        X[i][6]=(data["x"][i])**3
        X[i][7]=(data["y"][i])**3
        X[i][8]=(data["x"][i]**2)*data["y"][i]  
        X[i][9]=(data["x"][i])*(data["y"][i]**2)
    a=np.linalg.inv(np.dot(np.transpose(X),X))
    aa=np.dot(a,X.T)
    beta=np.dot(aa,D)
    x=np.linspace(0,15,100)
    y=np.linspace(0,15,100)
    gridx,gridy=np.meshgrid(x,y)
    gridepth=beta[0]+beta[1]*gridx+beta[2]*gridy+beta[3]*(gridx**2)+beta[4]*(gridy**2)+\
        beta[5]*gridx*gridy+beta[6]*(gridx**3)+beta[7]*(gridy**3)+\
        beta[8]*(gridx**2)*gridy+beta[9]*gridx*(gridy**2)
    return gridepth

#scatter plot
fig,ax=plt.subplots(figsize=(7,7))
axes=ax.scatter(data["x"],data["y"],c=data["d"],cmap="gist_earth")
ax.set_xlabel("position")
ax.set_ylabel("position")
ax.set_title("Data Point")
cbar=fig.colorbar(axes)
cbar.set_label("altitude (km)")

#grid plot
x=np.linspace(0,15,100)
y=np.linspace(0,15,100)
gridx,gridy=np.meshgrid(x,y)
gridepth=plane_regression_order3(data)
fig,ax=plt.subplots(figsize=(7,7))
axes=ax.contourf(gridx,gridy,gridepth,cmap="gist_earth")
axes_l=ax.contour(gridx,gridy,gridepth,colors="dimgray")
ax.set_xlabel("position_x")
ax.set_ylabel("position_y")
ax.set_title("Order of 3")
ax.clabel(axes_l, inline=True, fontsize=10,colors="black")
cbar=fig.colorbar(axes)
cbar.set_label("altitude (km)")
