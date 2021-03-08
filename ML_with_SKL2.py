# 보스턴 짒값 예측(평균값x, 중앙값)/ 제공 데이터 사용
import numpy as np
from sklearn.datasets import load_boston
boston_data = load_boston()
# 데이터 확인
print(boston_data.feature_names)
print(boston_data['feature_names'])
import pandas as pd
boston_pd = pd.DataFrame(boston_data.data, columns = boston_data.feature_names)
# Add target
boston_pd['MEDV'] = boston_data.target # 중간값
boston_pd.head()
# 빈 값 확인
boston_pd.isnull().sum()
# 데이터 시각화 
import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(boston_pd['MEDV'])
plt.show()
sns.distplot(boston_pd)
plt.show()
# feature와 target 상관관계 확인
correlation_matrix = boston_pd.corr().round(2)
plt.figure(figsize = (5, 5)) # 크기 변경
sns.heatmap(data = correlation_matrix, annot =True) # sns.heatmap(data = , annot = ) # 숫자값
plt.show() # 하얀색에 가까울 수록 상관관계가 높다.
# feature간의 상관관계가 높으면 빼주는 게 좋음(좀 일반적이라 할 수 있음)
# x와 y 분리
x_ = boston_pd.drop(['MEDV','NOX','DIS','TAX'], axis=1) # 기준  0 or 1, 0이면 index, 1이면 columns
y_ = boston_pd['MEDV']    
print(x_.shape, y_.shape)
# 데이터셋 분리
from sklearn.model_selection import train_test_split       # 학습이 80%      # 데이터를 고정
x_train, x_test, y_train, y_test = train_test_split(x_, y_, test_size = 0.2, random_state = 119)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# 데이터 정규화 과정 # feature간의 차이가 심하면 학습이 어려울수도, 언더_오버 플로 일어날 수 있음
# Scaling_Normalization
# StandardScaleWrapper > 평균과 표준편차
# MInMaxscaler > 0 ~ 1
# MaxAbsScaler > 절대값 -1 ~ 1 > 갑툭튀에 안좋음
# RobustScaler > 중앙값을 이용 > 분포에 맞게 > 갑툭튀에 사용
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
print(x_train[0:3])
# 학습
from sklearn.linear_model import LinearRegression
lin_model = LinearRegression()
lin_model.fit(x_train,y_train)
# 평가
y_predict = lin_model.predict(x_test)
from sklearn.metrics import mean_squared_error , r2_score
mse = mean_squared_error(y_test, y_predict)
r2 = r2_score(y_test, y_predict)
print(mse, r2)
# 시각화
plt.scatter(y_test, y_predict)
plt.plot([0,50],[0,50], "--k") # 범위
plt.tight_layout()