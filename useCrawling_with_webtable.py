import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd

y = str(input('년도(2009 ~ 2021) : '))
img = {'리오넬 메시' : './Images/Lionel_Messi.jpg', '카림 벤제마' : './Images/Karim_Benzema.jpg', '루이스 수아레스' : './Images/수아레스.jpg', '크리스티아누 호날두' : './Images/Ronaldo.jpg'}
table = pd.read_html('https://sports.news.naver.com/wfootball/record/index?category=primera&tab=player&year=' + y)
df = pd.DataFrame(table[0])
df_name = df.loc[0][1]
df_null = " "
df_realname = ''
for i in range(20):
  df_null = df_name[i-1]
  if(df_null == " " and df_name[i] == " "):
    break
  else:
    df_realname += df_name[i]
img_dic = img[df_realname.rstrip()]
path = img_dic
image_pil = Image.open(path)
image = np.array(image_pil)
image_py = np.array(image)
plt.title(df_realname)
plt.imshow(image_py)