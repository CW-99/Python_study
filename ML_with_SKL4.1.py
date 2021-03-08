# clustering with csv file
import pandas as pd
data = pd.read_csv("iris.csv")
# data 타입 변경
data.loc[data["variety"] == "Setosa","variety" ] = 0 
data.loc[data["variety"] == "Virginica","variety" ] = 2
data.loc[data["variety"] == "Versicolor","variety" ] = 1
import numpy as np
x = data.drop(["variety"], axis = 1)
y = data["variety"]
x = np.array(x) # numpy 형태로 바꾸는 게 필요
y = np.array(y)
# 시각화
import matplotlib.pyplot as plt
plt.scatter(x[:,1],x[:,2], c = y)
plt.xlabel("Sepal length", fontsize = 15)
plt.ylabel("Sepal width",fontsize = 15)
plt.show()
# 학습
from sklearn.cluster import KMeans
km = KMeans(n_clusters = 3, random_state = 222 )
km.fit(x)
new_label = km.labels_
print(new_label)
# 시각화
fig, axes = plt.subplots(1, 2, figsize = (16,8))
axes[0].set_title("Actual", fontsize = 15)
axes[0].scatter(x[:,0],x[:,1], c = y, s = 150 )
axes[1].set_title("Predicted", fontsize = 15 )
axes[1].scatter(x[:,0],x[:,1], c = new_label, cmap ='jet' , s = 150 )