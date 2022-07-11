import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score


## 導入數據集
dataset = pd.read_csv("linear_regression_dataset_sample.csv")
X = dataset.iloc[:, 1].values.reshape(-1,1)
y = dataset.iloc[:,2].values

## 將數據集拆成訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


## 訓練多項式迴歸模型
regressor = make_pipeline(PolynomialFeatures(degree=4), LinearRegression())
regressor.fit(X_train,y_train)
w_0 = regressor[1].intercept_
w_1 = regressor[1].coef_
print('Interception : ', w_0)
print('Coeficient : ', w_1)

## 迴歸模型的準確度
y_pred=regressor.predict(X_test)
print("Mean squared error: ",mean_squared_error(y_test, y_pred))
print("r2 score: ",r2_score(y_test, y_pred))

plt.scatter(X_train,y_train)
plt.plot(np.arange(1,16,0.1).reshape(-1,1), regressor.predict(np.arange(1,16,0.1).reshape(-1,1)))
plt.title('Salary vs Learning Hours')
plt.xlabel("Hours of Learning per Month")
plt.ylabel("Salary")
plt.show()

#different degree regression
fig,ax=plt.subplots(figsize=(14,14))
ax.scatter(X_train,y_train)
for degree in [2,3,4,5,6]:
    regressor = make_pipeline(PolynomialFeatures(degree=degree), LinearRegression())
    regressor.fit(X_train,y_train)
    ## 迴歸模型的準確度
    y_pred=regressor.predict(X_test)
    print(f"degree: {degree} r2score: ",r2_score(y_test, y_pred))

    ax.plot(np.arange(1,16,0.1).reshape(-1,1), regressor.predict(np.arange(1,16,0.1).reshape(-1,1)),label=f"degree: {degree}")
ax.set_title('Salary vs Learning Hours')
ax.set_xlabel("Hours of Learning per Month")
ax.set_ylabel("Salary")
ax.legend()


