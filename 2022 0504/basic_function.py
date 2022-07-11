
#自由落體公式： s = v0t + 1/2at^2

def drop(v0,t,a=9.8):
    s = v0*t + 0.5*a*t**2
    return s

distance=drop(0,10,9.8)
drop(t=5,v0=0,a=9.8)
drop(0,5)


#plot waveform function：
import pandas as pd
import matplotlib.pyplot as plt

file_name="201801012010_TTN_13012010.P18.asc"
waveform=pd.read_csv(f"{file_name}",sep="\s+",header=None,names=["Time","Z","H1","H2"])

def plot_waveform(waveform,file_name):
    fig,ax=plt.subplots(3,1,figsize=(10,7))
    ax[0].plot(waveform["Time"],waveform["Z"])
    ax[1].plot(waveform["Time"],waveform["H1"])
    ax[2].plot(waveform["Time"],waveform["H2"])
    ax[0].set_title(f"{file_name}")
    ax[2].set_xlabel("Time")
    ax[1].set_ylabel("amplitude")
    
    return fig


figure=plot_waveform(waveform,file_name)

