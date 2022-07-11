import pandas as pd
import matplotlib.pyplot as plt
import os


#Question 1:
file_list=os.listdir("waveforms")

for file in file_list:
    waveform=pd.read_csv(f"waveforms/{file}",sep="\s+",header=None,names=["Time","Z","H1","H2"])

    fig,ax=plt.subplots(3,1,figsize=(10,7))
    ax[0].plot(waveform["Time"],waveform["Z"])
    ax[1].plot(waveform["Time"],waveform["H1"])
    ax[2].plot(waveform["Time"],waveform["H2"])
    ax[0].set_title(f"{file}")
    ax[2].set_xlabel("Time")
    ax[1].set_ylabel("amplitude")

#Question2
catalog=pd.read_excel("C:/Users/user/Desktop/2017-2019 catalog.xlsx")

magnitude_filter=(catalog["ML"]>=4.5)

new_catalog=catalog[magnitude_filter]

# Year=[2017,2018,2019]
# Index=[1,2,3]
# for year,index in zip(Year,Index):
#     print(index,year)

figure=plt.figure(1,figsize=(30,20))

ax1 = plt.subplot(2,3,1) 
ax1.scatter(new_catalog[new_catalog["Year"]==2017]["Lon.X"], new_catalog[new_catalog["Year"]==2017]["Lat.Y"])
ax1.set_title("2017 earthquake magnitude ≥ 4.5",fontsize=20)
ax1.set_xlabel("Latitude",fontsize=15)

ax2 = plt.subplot(2,3,2)
ax2.scatter(new_catalog[new_catalog["Year"]==2018]["Lon.X"], new_catalog[new_catalog["Year"]==2018]["Lat.Y"])
ax2.set_title("2018 earthquake magnitude ≥ 4.5",fontsize=20)
ax2.set_ylabel("Lontitude",fontsize=15)
ax2.set_xlabel("Latitude",fontsize=15)

ax3 = plt.subplot(2,3,3)
ax3.scatter(new_catalog[new_catalog["Year"]==2019]["Lon.X"], new_catalog[new_catalog["Year"]==2019]["Lat.Y"])
ax3.set_title("2019 earthquake magnitude ≥ 4.5",fontsize=20)

ax4 = plt.subplot(2,1,2)
ax4.hist(new_catalog["ML"],bins=30,alpha=0.7)
ax4.set_title("2017-2019 earthquake distribution",fontsize=25)
ax4.set_ylabel("number of event",fontsize=20)
ax4.set_xlabel("magnitude",fontsize=20)

# figure.savefig("Question2.png",dpi=300)


#Question3:
iris=pd.read_excel("Dataframe/IRIS catalog.xlsx")
gcmt=pd.read_excel("Dataframe/GCMT catalog.xlsx")

new_catalog=pd.merge(iris,gcmt,
                        left_on=['Year', 'Month', 'Date', 'Hour', 'Minute'],\
                        right_on=['GCMT_Year', 'GCMT_Month', 'GCMT_Date', 'GCMT_Hour', 'GCMT_Minute'],\
                        how="left")

new_catalog.to_excel("Dataframe/merge_catalog.xlsx")