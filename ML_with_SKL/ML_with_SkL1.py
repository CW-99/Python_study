import numpy as np
year, temp_diff = np.loadtxt('5-year-mean-1882-2014.csv', delimiter = ",", usecols = (0,1), unpack = True)
# 데이터 확인
print(year[:9])
print(temp_diff[:9])
# 데이터 시각화
import matplotlib.pyplot as plt
plt.scatter(year, temp_diff)
plt.title("scatter plot of temp_diff as year ")
plt.xlabel("Year")
plt.ylabel("Temp_diff")
plt.show()
# shape 확인 
print(year.shape, temp_diff.shape) # year의 shape를 변경해줘야함
year = year.reshape(133,1)
print(year.shape)
# Regression model
from sklearn.linear_model import LinearRegression
linear_model = LinearRegression(fit_intercept = True) # Y절편 여부
linear_model.fit(year, temp_diff) # feature 과 타겟값
model_predict = linear_model.predict(year)
print(model_predict[0:9])
# 모델 시각화
plt.scatter(year, temp_diff) # 산점도.
plt.plot(year, model_predict) # 직선
plt.title("real temp_diff cs model_predicted_diff")
plt.show()
# 모델 확인
print("Y={}X{}".format(linear_model.coef_[0], linear_model.intercept_)) # 기울기와 Y절편
# 기울기가 여러 개가 나올 수 있기 때문에 index로 하나만 가져오기.