import pandas as pd
import matplotlib.pyplot as plt

catalog=pd.read_excel("2020 catalog.xlsx")

magnitude_mask=(catalog["ML"]>=4)
catalog=catalog[magnitude_mask]
depth_mask=(catalog["Depth"]>=35)

subduction_catalog=catalog[depth_mask]
others_event_catalog=catalog[~depth_mask]


fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(projection='3d')
ax.scatter(others_event_catalog["Lon.X"],others_event_catalog["Lat.Y"],\
            others_event_catalog["Depth"],s=2.5,label="Crust Events")
# ax.scatter(others_event_catalog["Lon.X"],others_event_catalog["Lat.Y"],\
#             others_event_catalog["Depth"],label="Crust Events")
ax.scatter(subduction_catalog["Lon.X"],subduction_catalog["Lat.Y"],\
            subduction_catalog["Depth"],c="orange",s=2.5,label="Subduction Events")
# ax.scatter(subduction_catalog["Lon.X"],subduction_catalog["Lat.Y"],subduction_catalog["Depth"],\
#             c="orange",label="Subduction Events")
ax.set_xlabel("Lontitude",fontsize=13)
ax.set_ylabel("Latitude",fontsize=13)
ax.set_zlabel("Depth (km)",fontsize=13)
ax.set_title(f"2020 Taiwan Events",fontsize=18)
# ax.set_title(f"2020 ML >= 4 Taiwan Events",fontsize=18)
ax.view_init(elev=20,azim=10)
ax.invert_zaxis()
ax.legend(loc="best")