import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

catalog=pd.read_excel("2017-2019 catalog.xlsx")

magnitude_mask=(catalog["ML"]>=3.5)

target_catalog=catalog[magnitude_mask]

Magnitude=[3.5,4,4.5,5,5.5,6]
magnitude_counts=[]
for magnitude in Magnitude:
    mask=((target_catalog["ML"]>=magnitude) & (target_catalog["ML"]<magnitude+0.5))
    magnitude_counts.append(len(target_catalog[mask]["ML"]))

Magnitude=np.array(Magnitude)
magnitude_counts=np.array(magnitude_counts)
magnitude_counts_log=np.log10(magnitude_counts)

#plot number of event and magnitude
fig,ax=plt.subplots(figsize=(7,7))
ax.scatter(Magnitude,magnitude_counts_log)
ax.set_xlabel("Magnitude",fontsize=12)
ax.set_ylabel("log10(N)",fontsize=12)
ax.set_title("Number of event (N) vs Magnitude",fontsize=15)

#linear regression
model=LinearRegression()
model.fit(Magnitude.reshape(-1,1),magnitude_counts_log)
a = model.intercept_
b = model.coef_
print(f"GR-Law regression: log10(N)={np.round(a,3)}{np.round(b[0],3)}*M")
count_predicted=model.predict(Magnitude.reshape(-1,1))
r2score=np.round(r2_score(magnitude_counts_log, count_predicted),3)

#plot GR-Law
fig,ax=plt.subplots(figsize=(7,7))
ax.scatter(Magnitude,magnitude_counts_log)
ax.plot(Magnitude,count_predicted,c="red")
ax.text(5.3,3,f"R2 score:{r2score}",fontsize=12)
ax.set_title(f"GR-Law regression: log10(N)={np.round(a,3)}{np.round(b[0],3)}*M",fontsize=15)
ax.set_xlabel("Magnitude",fontsize=12)
ax.set_ylabel("log10(N)",fontsize=12)
