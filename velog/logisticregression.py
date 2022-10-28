import pandas as pd

# 타이타닉 예제
titanic = pd.read_csv("파일명")


#-------------------------- 데이터 전처리 -------------------------------------
# 문자열 숫자로 변환
titanic['Sex'] = titanic['Sex'].map({'female':1, 'male':0})

# 결측치 채우기
titanic['Age'].fillna(value=titanic['Age'].mean(), inplace=True)

# feature 분리
titanic['FirstClass'] = titanic['Pclass'].apply(lambda x:1 if x == 1 else 0)
titanic['SecondClass'] = titanic['Pclass'].apply(lambda x:1 if x == 2 else 0)
#------------------------------------------------------------------------------

from sklearn.model_selection import train_test_split

train_features, test_features, train_labels, test_labels = train_test_split(features, survival)


# 데이터 정규화(스케일링) 하기
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

train_features = scaler.fit_transform(train_features)
test_features = scaler.transform(test_features)

# 모델 생성 및 평가
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(train_features, train_labels)

print(model.score(train_features, train_labels))

print(model.score(test_features, test_labels))



import numpy as np

Jack = np.array([0.0, 20.0, 0.0, 0.0])
Rose = np.array([1.0, 17.0, 1.0, 0.0])
ME = np.array([0.0, 32.0, 1.0, 0.0])

sample_titanic = np.array([Jack, Rose, ME])
sample_titanic = scaler.transform(sample_titanic)
print(model.predict(sample_titanic))