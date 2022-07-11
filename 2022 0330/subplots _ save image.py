import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#subplots example1:

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(2, 2,figsize=(14,7))
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Axis [0,0]')
axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0,1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1,0]')
axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1,1]')

#subplots example2

t1 = np.arange(0.0, 3.0, 0.01)

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

figure=plt.figure(1,figsize=(7,7))

#第一個數字代表row，第二的數字代表column，第三個數字代表要在第幾個位置
ax1 = plt.subplot(2,1,2) 
ax1.plot(t1, f(t1),c="blue")
ax1.set_title("blue line")

ax2 = plt.subplot(2,2,2)
ax2.plot(t1, f(t1),c="orange")
ax2.set_title("orange line")

ax3 = plt.subplot(2,2,1)
ax3.plot(t1, f(t1),c="green")
ax3.set_title("green line")

#subplots waveforms example:
file_list=os.listdir("waveforms")

for file in file_list:
    waveform=pd.read_csv(f"waveforms/{file}",sep="\s+"\
                        ,header=None,names=["Time","Z","H1","H2"])

    fig,ax=plt.subplots(3,1,figsize=(10,7))
    ax[0].plot(waveform["Time"],waveform["Z"])
    ax[1].plot(waveform["Time"],waveform["H1"])
    ax[2].plot(waveform["Time"],waveform["H2"])
    ax[2].set_xlabel("Time",fontsize=20)
    ax[1].set_ylabel("Amp.",fontsize=20)
    ax[0].set_title(f"{file}",fontsize=25)
    fig.savefig(f"waveforms/{file}.pdf",dpi=300)

#save figure
figure.savefig("example.png",dpi=300)
# figure.savefig("example1.png",dpi=10)