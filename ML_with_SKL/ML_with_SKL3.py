# Classification # with Titaninc data
import pandas as pd
data = pd.read_csv("Titanic_dataset.csv")
# describe로 데이터 확인하기.
data.describe(include = "all") # include = 'all' > 전체 데이터 
# 빠진 값 확인하기
data.isnull().sum()
# feature 제거
data.drop(["cabin",'boat','body','home.dest','name','ticket']
          ,axis =1, inplace = True) # inplace > data의 원본 수정
          # 데이터 채우기 (변경) (숫자값)     # 조건()을 만족하는 low 선택, 그 중에서 가져오고 싶은 columns
data.loc[data.fare.isnull(), ['fare']] = data.fare.mean()
data.loc[data['age'].isnull(), 'age'] = data.age.mean()
# 동시에 변경 불가
# 데이터 채우기 (글자) 
data.groupby('embarked').size()
data.loc[data.embarked.isnull(), "embarked"] = "S"
print(data.groupby('embarked').size())
# null값 다시 확인 > 없음
data.isnull().sum()
# 시각화
import seaborn as sns
import matplotlib.pyplot as plt  # 0 or 1
print(data.survived.value_counts(normalize = True)) # (normalize = True) > 한 번에 보여줌
sns.countplot(data.survived) # 막대그레프
plt.title('Count of surviver')
# 성별에 따른 생존자 수   ( X, hue =  Y )
sns.countplot(data.gender, hue = data.survived)
plt.title("Relationship between gender and surviver")
# 선실 등급에 따른 생존 여부
#     등고선    x             y           
sns.kdeplot(data.pclass, data.survived)
plt.title("Relationship between pclass ans surviver")
# 데이터 변환 글자 > 숫자
data.loc[data.gender=='male',['gender']] = 0
data.loc[data.gender=='female','gender'] = 1

data.loc[data.embarked=='S','embarked'] = 0
data.loc[data.embarked=='Q','embarked'] = 1
data.loc[data.embarked=='C','embarked'] = 2
# X와 Y분리 후 확인
X = data.drop("survived", axis = 1)
Y = data.survived
print(X[:4])
print(Y[:4])
# 데이터셋 분리
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 111)
# 학습
from sklearn.linear_model import LogisticRegression
log_classifier = LogisticRegression()
log_classifier.fit(X_train, Y_train)
# 평가
from sklearn.metrics import accuracy_score # 정확도
y_predict = log_classifier.predict(X_test)
acc = accuracy_score(Y_test, y_predict)
print(acc)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_predict)
sns.heatmap(cm, annot = True)