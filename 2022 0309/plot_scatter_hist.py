import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.arange(10)
y=np.arange(10)

plt.plot(x,y)
plt.scatter(x,y,color="red")

#===============================
fig,ax=plt.subplots(figsize=(7,7))
ax.plot(x,y)
ax.scatter(x,y,color="red")
ax.set_ylabel("This is x")
ax.set_xlabel("This is y")
ax.set_title("This is title")

#error 示範

#===============================
data=pd.read_excel("./sample.xlsx")
type(data)
data.dtypes
data.head()
data.columns
data.index
data["微積分成績"]
data.loc[["微積分成績","應數成績"]]
data.isna().sum()

fig,ax=plt.subplots(figsize=(7,7))
ax.hist(data["微積分成績"],bins=20)
ax.set_xlabel("score")
ax.set_ylabel("number of students")
ax.set_title("freshman calculas score distribution")

fig,ax=plt.subplots(figsize=(7,7))
ax.hist(data["微積分成績"],bins=20,alpha=0.5)
ax.hist(data["應數成績"],bins=20,alpha=0.5)
ax.set_xlabel("score")
ax.set_ylabel("number of students")
ax.set_title("freshman score distribution")
ax.set_xlim(0,100)
ax.legend(["caculas score","math score"])

#====================================

filter1=(data["微積分成績"]>60)
filter2=((data["微積分成績"]>=50) & (data["微積分成績"]<60))
filter3=(data["微積分成績"]<50)
counts1=data[filter1]["微積分成績"].value_counts().sum()
print("及格人數:",counts1)
counts2=data[filter2]["微積分成績"].value_counts().sum()
print("可能被救的人數:",counts2)
counts3=data[filter3]["微積分成績"].value_counts().sum()
print("會被當人數:",counts3)
plt.pie([counts1,counts2,counts3],labels=["pass","maybe pass","can not pass"],autopct="%1.1f%%")


filter4=((data["微積分成績"]<60) & ((data["應數成績"]>60)))
data.loc[data["應數成績"]<40]
data.loc[data["應數成績"]<40].index

data.loc[filter4,["應數成績"]]
data.loc[filter4,["微積分成績"]].index

data.loc[filter4,["大一到大二的轉變"]]="數學及格了"






