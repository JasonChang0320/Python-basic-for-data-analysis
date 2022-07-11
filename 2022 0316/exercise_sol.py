import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

catalog=pd.read_excel("2020 catalog.xlsx")

#Question1: quality visualization
fig,ax=plt.subplots(figsize=(7,7))
ax.hist(catalog["quality"])
ax.set_ylabel("number of events")
ax.set_xlabel("Quality")
ax.set_title("CWB catalog quality")

#Question2: magnitude > 4.5 events position
magnitude_mask=(catalog["ML"]>=4.5)
filtered_catalog=catalog[magnitude_mask]

fig,ax=plt.subplots(figsize=(7,7))
ax.scatter(filtered_catalog["Lon.X"],filtered_catalog["Lat.Y"])
ax.set_ylabel("Latitude")
ax.set_xlabel("Lontitude")
ax.set_title("2020 CWB catalog magnitude > 4.5 map")

#Question3: Quqlity and magnitude relationship

catalog.loc[catalog["quality"]=="A",["quality_number"]]=4
catalog.loc[catalog["quality"]=="B",["quality_number"]]=3
catalog.loc[catalog["quality"]=="C",["quality_number"]]=2
catalog.loc[catalog["quality"]=="D",["quality_number"]]=1

fig,ax=plt.subplots(figsize=(14,7))
ax.scatter(catalog["ML"],catalog["quality_number"],s=10,alpha=0.5)
ax.set_xlabel("Magnitude (ML)")
ax.set_ylabel("Time")
ax.set_title("2020 CWB catalog")
ax.set_yticks([1,2,3,4])
ax.set_yticklabels(["D","C","B","A"])
