import pandas as pd
from bs4 import BeautifulSoup
import requests
from openpyxl.workbook import Workbook

apikey = 'BzEMUSnzGI%2BOWOTv%2F2PjTzUYm%2F9TAbc4IDMiro6sHuPa7zMQXfx%2FVwYTogvzt63BdnW%2FnF%2BhvIqxnVvCsH60jA%3D%3D' # api 키


api1 = "http://apis.data.go.kr/B552584/EvCharger/getChargerInfo?serviceKey=BzEMUSnzGI%2BOWOTv%2F2PjTzUYm%2F9TAbc4IDMiro6sHuPa7zMQXfx%2FVwYTogvzt63BdnW%2FnF%2BhvIqxnVvCsH60jA%3D%3D"
api2 = "&numOfRows=10&pageNo="

list_drugs = ['충전소명', '주소', '위도', '경도', '이용가능시간', '지역코드']
Nm = []
address = []
lat = [] # 위도
lon = [] # 경도
ti = []
co = []

# 각종 리스트 선언

for i in range(1, 6):
  api =  api1 + api2 + str(i) # 실제로 사용하는 Api, 제일 뒤에 pageNo= 이 반복문은 통해 바뀜
  for list_drug in list_drugs:
    url = api.format(list_drugs=list_drug, key=apikey)
    req= requests.get(url)
    re = req.text
    soup = BeautifulSoup(re, 'html.parser')

    # 충전소명
    Nm += soup.find_all('statnm')
    # 주소
    address += soup.find_all('addr')
    # 위도
    lat += soup.find_all('lat')
    # 경도
    lon += soup.find_all('lng')
    # 이용가능시간
    ti += soup.find_all('usetime')
    # 지역코드
    co += soup.find_all('zcode')

n = []
a = []
l = []
lo = []
t =[]
c=[]

for i in range(len(Nm)):
  n.append( Nm[i].get_text())
  a.append(address[i].get_text())
  l.append(float(lat[i].get_text()))
  lo.append(float(lon[i].get_text()))
  t.append(ti[i].get_text())
  c.append(co[i].get_text())
  
# 리스트에 문자열 값으로 넣음

pd.Series(n)
pd.Series(a)
pd.Series(t)
pd.Series(c)
pd.Series(l)
pd.Series(lo)

# 시리즈 타입으로 변환


df = pd.DataFrame({'Name': n, 'Addr':a, 'Latitude':l, 'Longitude':lo, 'Time' : t, 'Code':c})

# df라는 데이터프레임을 만듦. 

import plotly.express as px 
fig = px.scatter_mapbox( df, lat='Latitude', lon='Longitude', 
hover_name = 'Name', hover_data=['Addr', 'Time']
,color_discrete_sequence=['fuchsia'], zoom=5, height=400)
fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(margin={'r':0, 't':0, 'l':0, 'b':0})
fig.show()

# 지도를 그림