import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# =================================
print(a)
# [[ 1  2  3  4]
# [ 5  6  7  8]
# [ 9 10 11 12]]
print(np.shape(a))
# (3,4)
a.shape = (6,2) # 6줄, 2칸
print(a)
# [[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]
#  [11 12]]

# ==================================

# ========== 행열 연산 ==============
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.ones(3, dtype=int) # 1로 3개 행을 만듬

print(b)
# > [1 1 1]

print(a + b)
# > [[2 3 4],[5 6 7],[8 9 10]]
print(a - b)
# > [[0 1 2],[3 4 5],[6 7 8]]
print(a * b)
# > [[1 2 3],[4 5 6],[7 8 9]]
print(a / b)
# > [[1. 2. 3.], [4. 5. 6.], [7. 8. 9.]]

print(a @ b) # 합성곱
# > [6 15 24]

# 합성곱이란
# 이미지의 형상을 무시하지 않고 이미지를 그대로 인공 신경망이 학습할 수 있게 해주는 수학 행렬 연산
# 참고 : https://lsh-story.tistory.com/48
# ====================================

# ============= 숫자 7 ================
seven = np.array([[0,1,1,1,0],[0,1,0,1,0], [0,0,0,1,0],[0,0,0,1,0],[0,0,0,1,0]]) # 7 숫자

A = np.array([[0,0,0],[1,1,1],[0,0,0]])# 합성곱 할 것
S = [] # 결과값
for i in range(3):
  for j in range(3):
      B = seven[i:i+3,j:j+3]
      # 행렬을 1씩 움직여서 seven은 5x5이지만 합성곱을 할 수 있도록 3x3으로 쪼개는 것
      S.append((B @ A).sum())
      # 합성곱한 행렬에서 총합을 S에 추가함

print(S)
# > [6, 3, 9, 3, 0, 9, 0, 0, 9]
S = np.array(S).reshape(3,3)
# > S의 형태를 3x3으로 변형함
print(S)
# > [[6 3 9]]
# >  [3 0 9]
# >  [0 0 9]]

if(S[1][1]):
  print('True')
else:
  print('Fail')

# > Fail


imgData2 = np.zeros((3,3,3)) # 0으로 채워진 3개의 3x3인 array가 생성됨
for i in range(len(S)): # len(S) = 3
  for j in range(len( S[i]) ): #S[0] : array([6, 3, 9]), S[1] : array([3,0,9]), S[2] : array([0,0,9])
    if S[i][j]:
      imgData2[i][j] = [ S[i][j] * 0.1, 0,0] # 빨간색
    else:
      imgData2[i][j] = [1,1,1]


import matplotlib.pyplot as plt

fig = plt.figure()
plt.imshow(imgData2)
plt.show()

# ================================================