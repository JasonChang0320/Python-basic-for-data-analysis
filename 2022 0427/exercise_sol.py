import pygmt as gmt
import pandas as pd

catalog=pd.read_csv("merge_event_eq.csv")
catalog.sort_values(by="Mag", ascending=False,inplace=True)
catalog["Depth(km)"]=catalog["Depth(m)"]/1000

#step 1
MMgrid = gmt.datasets.load_earth_relief(resolution="01m",\
    region=[92, 102.5, 8, 28.5])
fig = gmt.Figure()
fig.grdimage(grid=MMgrid,projection="M15c",cmap="gray") #cmap="geo"
fig.coast(shorelines="1p,black",water="white",borders="1/0.75p,black")
fig.basemap(frame=["a",'+t"Myanmar earthquake in 2016-2021"'])
# fig.show()

#step 2
# gmt.makecpt(cmap="viridis", series=[data["Depth"].min(), data["Depth"].max()])
gmt.makecpt(cmap="custom.cpt", series=[catalog["Depth(km)"].min(), catalog["Depth(km)"].max()])

fig.plot(
    x=catalog["Lon"],
    y=catalog["Lat"],
    style="cc", 
    pen="black",
    size =0.02* 1.75 **catalog["Mag"],
    color=catalog["Depth(km)"],
    cmap=True,
    transparency=50
)
fig.colorbar(frame='af+l"Depth (km)"')
# fig.show()

#step 3

#建立假的資料當作legend
mag_legend=pd.DataFrame([3,4,5,6,7],columns=["magnitude"])
mag_legend["lon"]=[101.75,101.75,101.75,101.75,101.75]
mag_legend["lat"]=[8.3,8.75,9.2,9.8,10.6]

#繪製 legend
fig.plot(
    x=mag_legend["lon"],
    y=mag_legend["lat"],
    style="cc",
    pen="black",
    size =0.02* 1.75 **mag_legend["magnitude"],
    color="green",
    transparency=50
)
fig.text(
    x=101.5,
    y=11.5,
    text="Magnitude",
    font="12p"
)
fig.text(
    x=mag_legend["lon"]-0.7,
    y=mag_legend["lat"],
    text=mag_legend["magnitude"]
)
# fig.show()
#繪製比例尺
fig.plot(x=[94,96], y=[9.5,9.5], pen="1.25p", style=f"f1c/0.25c")
fig.text(
        x=95,
        y=9,
        text="200 km",
        font="12p"
    )
# fig.show()
#繪製指北針
fig.plot(
    x=101.75, y=25.75, style="v1c+e+h0.5", direction=([90], [2]), pen="2p", color="red3"
    ) # direction=([angle], [length])
fig.text(
    x=101.75, y=27.25,
    text="N",
    font="15p"
    )
fig.show()