import pygmt as gmt
import pandas as pd


data=pd.read_csv(f"2018 eq data.txt")
data.sort_values(by="Final_Mw", ascending=False,inplace=True)

#step 1
TWgrid = gmt.datasets.load_earth_relief(resolution="15s",\
    region=[118, 124.5, 20, 26])
fig = gmt.Figure()
fig.grdimage(grid=TWgrid,projection="M15c",cmap="gray") #cmap="geo"
fig.coast(shorelines="1p,black",water="white")
fig.basemap(frame=["a",'+t"Taiwan"'])
# fig.show()

#step 2
# gmt.makecpt(cmap="viridis", series=[data["Depth"].min(), data["Depth"].max()])
gmt.makecpt(cmap="custom.cpt", series=[data["Depth"].min(), data["Depth"].max()])

fig.plot(
    x=data["Lon"]+(data["Lon.min"]/60),
    y=data["Lat"]+(data["Lat.min"]/60),
    style="cc", 
    pen="black",
    size =0.02* 1.75 **data["Final_Mw"],
    color=data["Depth"],
    cmap=True,
    transparency=50
)
fig.colorbar(frame='af+l"Depth (km)"')
# fig.show()

#step 3

#建立假的資料當作legend
mag_legend=pd.DataFrame([3.5,4,5,6,7],columns=["magnitude"])
mag_legend["lon"]=[124,124,124,124,124]
mag_legend["lat"]=[21,21.25,21.5,21.78,22.25]

#繪製 legend
fig.plot(
    x=mag_legend["lon"],
    y=mag_legend["lat"],
    style="cc",
    pen="black",
    size =0.02* 1.75 **mag_legend["magnitude"],
    color="darkblue",
    transparency=50
)
fig.text(
    x=124,
    y=22.65,
    text="Mw",
    font="15p"
)
fig.text(
    x=mag_legend["lon"]-0.5,
    y=mag_legend["lat"],
    text=mag_legend["magnitude"]
)
#繪製比例尺
fig.plot(x=[119,119.5], y=[21,21], pen="1.25p", style=f"f1c/0.25c")
fig.text(
        x=119.25,
        y=20.75,
        text="50 km"
    )
#繪製指北針
fig.plot(
    x=124, y=25, style="v1c+e+h0.5", direction=([90], [1.75]), pen="2p", color="red3"
    ) # direction=([angle], [length])
fig.text(
    x=124, y=25.8, text="N",font="15p"
    )
fig.show()
