import random
import numpy as np

a = [] # 사과
p = [] # 배

#일반적으로 배가 사과보다 크고 무거움

for i in range(50): #50개의 데이터를 각각 추가함
  a.append([random.randint(5,10), random.randint(50,100), 1])
  p.append([random.randint(8,15), random.randint(90,120), 0])

# random.randint(a, b) -> 인자로 들어온 a,b 사이의 랜덤한 정수(int)를 반환함(a,b를 포함한 범위임)
# 마지막의 1과 0은 데이터 상에서 사과와 배를 구분하기 위함임

def distance(x, y):
  return np.sqrt(pow((x[0]-y[0]),2)+pow((x[1]-y[1]),2))

# sqrt -> numpy에서 제공하는 함수로, 제곱근 배열을 반환
# numpyt.sqrt(x, y = None)
# => x : 입력배열, y : y가 주어지면 결과는 y에 저장됨. y는 x와 같은 모양이어야함.
# pow(x, y) = x의 y승 = x ** y

def knn(x,y,k): # x = new, y = a+p, k = num
  result = []
  cnt = 0
  for i in range(len(y)):  # y-1번 => 99번
    result.append([distance(x,y[i]),y[i][2]]) # result 리스트에 distance 함수로 파라미터 x(new)와 a,p에 있는 각각의 리스트인 y[i]를 넘긴다.
    # distance의 return 값 ->  
  result.sort()
  for i in range(k):
    if result[i][1] == i:
      cnt += 1
  if cnt > (k/2):
    print("pear")
  else:
    print("apple")

size = input("크기 : ")
weight = input("무게 : ")
num = input("k : ")
new = [int(size), int(weight)]

knn(new, a+p, int(num)) # knn 함수 호출