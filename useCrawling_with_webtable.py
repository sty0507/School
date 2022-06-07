import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd

y = str(input('년도(2009 ~ 2021) : ')) # 년도 입력 받을 때 string 형태로 받음
img = {'리오넬 메시' : './Images/Lionel_Messi.jpg', '카림 벤제마' : './Images/Karim_Benzema.jpg', '루이스 수아레스' : './Images/수아레스.jpg', '크리스티아누 호날두' : './Images/Ronaldo.jpg'} # 출력을 위한 이미지 주소를 딕셔너리로 선언
table = pd.read_html('https://sports.news.naver.com/wfootball/record/index?category=primera&tab=player&year=' + y) # html에서 table 값을 받아옴
df = pd.DataFrame(table[0]) # dataframe으로 바꿔서 분석이 더 편하게 바꿔줌
df_name = df.loc[0][1] # 제일 위에 있는 사람의 이름과 팀이 나옴(ex '카림 벤제마  레알 마드리드')
df_null = " "
df_realname = ''
# 앞에 이름만 찾는 코드
for i in range(20):
  df_null = df_name[i-1]
  if(df_null == " " and df_name[i] == " "): # 이름과 팀 사이에 공백이 2칸임 -> 그걸 확인
    break
  else:
    df_realname += df_name[i]
img_dic = img[df_realname.rstrip()] # 하고 나면 '카림 벤제마 '와 같이 마지막에 공백이 존재 -> rstrip()함수로 마지막 문자 삭제

# =============이미지 출력을 위한 가공?===============
path = img_dic
image_pil = Image.open(path)
image = np.array(image_pil)
image_py = np.array(image)
# ===================================================

# 이미지 출력 by plt
plt.title(df_realname)
plt.imshow(image_py)