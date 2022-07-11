#Question1:

#Question2:
import numpy as np

answer=np.random.randint(1,20)

guess=int(input("please guess a number during 1,20 "))
print(guess)

#Question3:
import pandas as pd
import os
import matplotlib.pyplot as plt

data=pd.read_csv("waveforms/201801012010_TTN_13012010.P18.asc",sep="\s+",header=None)
data.columns=["Time","Vertical","H1","H2"]
file_list=os.listdir("./waveforms")