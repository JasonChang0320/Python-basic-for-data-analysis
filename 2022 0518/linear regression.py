import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


## 導入數據集
dataset = pd.read_csv("linear_regression_dataset_sample.csv")
X = dataset.iloc[:, 1].values.reshape(-1,1)
y =dataset.iloc[:,2].values

## 將數據集拆成訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

## 訓練與建構迴歸模型
regressor = LinearRegression()
regressor.fit(X_train, y_train)

## 計算出截距值與係數值
w_0 = regressor.intercept_
w_1 = regressor.coef_

print('Interception : ', w_0)
print('Coeficient : ', w_1)

## 迴歸模型的準確度
y_pred = regressor.predict(X_test)
print("Mean squared error: ",mean_squared_error(y_test, y_pred))
print("r2 score: ",r2_score(y_test, y_pred))

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Learning Hours')
plt.xlabel("Hours of Learning per Month")
plt.ylabel("Salary")
plt.show()
