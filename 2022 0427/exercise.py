import pandas as pd
import pygmt as gmt

data=pd.read_csv(f"2018 eq data.txt")
data.sort_values(by="Final_Mw", ascending=False,inplace=True)






#建立假的資料當作legend
mag_legend=pd.DataFrame([3,4,5,6,7],columns=["magnitude"])
mag_legend["lon"]=[101.75,101.75,101.75,101.75,101.75]
mag_legend["lat"]=[8.3,8.75,9.2,9.8,10.6]