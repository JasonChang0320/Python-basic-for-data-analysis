#Question1:
for a in range(1,10):
    for b in range(1,10):
        print(f"{a}*{b}={a*b}")

#Question2
import numpy as np

answer=np.random.randint(1,20)
guess=0
while guess!=answer:
    guess=int(input("please guess a number during 1,20 "))
    if guess> answer:
        print(f"{guess} bigger than answer")
    elif guess< answer:
        print(f"{guess} smaller than answer")
    else:
        print(f"Bingo! : answer is {answer}")

#Question 3:
import pandas as pd
import os
import matplotlib.pyplot as plt

file_list=os.listdir("waveforms")

for file in file_list:
    data=pd.read_csv(f"waveforms/{file}",sep="\s+",header=None)
    data.columns=["Time","Vertical","H1","H2"]
    fig,ax=plt.subplots(figsize=(14,7))
    ax.plot(data["Time"],data["Vertical"])
    ax.set_title(file)
    ax.set_xlabel("time")
    ax.set_ylabel("amplitude")
