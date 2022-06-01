방과후 머신러닝 시간에 한것들

## 1) useApi.py
한국환경공단에서 제공해주는 전기자동차 충전소 위치 api를 사용해서 데이터를 가공해서 scatter_mapbox라는 함수로 지도 위에 표시를 함.
이것으로 우리나라에 있는 전기자동차 충전소 위치를 알 수 있음.

- 코드 실행을 위해 해야될 것
```
pip install pandas
pip install bs4
pip install requests
pip install plotly==5.4.0
```

- 결과

![제출](https://user-images.githubusercontent.com/80656669/169822794-1e41613d-e53c-46f2-b6dd-b2f42eb20569.PNG)

## 2) useNumpy.py
Numpy라는 행렬 연산하는 라이브러리를 통해 이미지 데이터를 줄일 수 있게함


![numpy 7](https://user-images.githubusercontent.com/80656669/171404727-94a1e161-57b1-496a-9c7f-262f07e61559.PNG)



사용한 api : https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15076352
