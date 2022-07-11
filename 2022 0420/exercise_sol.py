import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Question1:
np.random.seed(1)
a=np.random.randint(1,20,(128,200))
b=np.random.randint(1,20,(200,2))

#1-1
axb=np.dot(a,b)

#1-2
new_axb=axb.reshape(16,16)

#1-3
axb_concated=np.concatenate((new_axb,a.reshape(16,-1)),axis=1)

#1-4
axb_concated=axb_concated.flatten()

x=np.arange(len(axb_concated))
fig,ax=plt.subplots()
ax.scatter(x,axb_concated,s=1)
# ax.set_yscale("log")


#Question2:
file_name="201801071953_CHKH_13071953.P18.asc"
waveform=pd.read_csv(file_name,sep="\s+",header=None)
waveform.columns=["Time","Vertical","H1","H2"]
p_picks=19.68       
s_picks=22.38

Waveform=np.array(waveform)
Time=Waveform[:,0]

p_pick_index=np.where(Time == p_picks)[0][0]
Waveform[p_pick_index+(5*100):,1:]=0

fig,ax=plt.subplots(3,1,figsize=(10,7))
ax[0].plot(Time,Waveform[:,1])
ax[1].plot(Time,Waveform[:,2])
ax[2].plot(Time,Waveform[:,3])
ax[0].axvline(p_picks,c="red")
ax[0].axvline(s_picks,c="yellow")
ax[1].axvline(p_picks,c="red")
ax[1].axvline(s_picks,c="yellow")
ax[2].axvline(p_picks,c="red")
ax[2].axvline(s_picks,c="yellow")
ax[2].set_xlabel("Time",fontsize=20)
ax[1].set_ylabel("amplitude",fontsize=20)
ax[0].set_title(file_name,fontsize=25)

