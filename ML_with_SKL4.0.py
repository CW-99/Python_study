# clustering # with iris data
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.keys())
print(iris.feature_names)
# 데이터 나누기
x = iris.data
y = iris.target
print(x.shape, y.shape)
# 시각화 - scatter 
import matplotlib.pyplot as plt
plt.scatter(x[:,1],x[:,2], c = y)
plt.xlabel("Sepal length", fontsize = 15)
plt.ylabel("Sepal width",fontsize = 15)
plt.show()
# 학습
from sklearn.cluster import KMeans
km = KMeans(n_clusters = 3, random_state = 20) # k 값 정하기
km.fit(x)
# Centroid 확인
centers = km.cluster_centers_
print(centers)
# 그룹 결과 확인 (kmeans에서 label 확인하기)
new_labels = km.labels_
print(new_labels)
# 결과 시각화        # 한 줄에 2개의 그래프
fig, axes = plt.subplots(1,2, figsize = (16,8))
axes[0].set_title("Actual", fontsize = 15)
axes[0].scatter(x[:,0],x[:,1], c = y, s = 150 ) # s = size, c = c 기반 색 다르게 (array형태나 컬러)
axes[1].set_title("Predicted", fontsize = 15 )
axes[1].scatter(x[:,0],x[:,1], c = new_labels, cmap ='jet' , s = 150)