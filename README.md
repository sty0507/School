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

사용한 api : https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15076352

## 2) useNumpy.py
Numpy라는 행렬 연산하는 라이브러리를 통해 이미지 데이터를 줄일 수 있게함


![numpy 7](https://user-images.githubusercontent.com/80656669/171404727-94a1e161-57b1-496a-9c7f-262f07e61559.PNG)


## 3) useCrawling_with_webtable.py
Pandas로 table 형태의 값을 가져옴

- 년도를 입력하면 그 해의 라리가 득점왕을 구해옴(pandas로 table 값을 가져와서)

![2014](https://user-images.githubusercontent.com/80656669/172333964-c0f494f5-996d-4929-bcb7-66a6f98a963d.PNG)<br>
이렇게 입력하면 <br>
![ro](https://user-images.githubusercontent.com/80656669/172333956-2d083279-fb70-48ca-8630-b9cc92d29aca.PNG)<br>
가 뜬다(박스 쳐져있는 이유는 한글 폰트 적용을 안함) 

폰트 적용코드 
```
# 한글이 깨지는 것을 막기 위해 글꼴을 설치해야 함
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
#런타임 다시 시작
```

![14-15](https://user-images.githubusercontent.com/80656669/172333966-8f52aeef-dfd9-4b0b-8212-76164d323d31.PNG)<br>
실제 값과 같다

이것들은 코랩 환경에서 해야 잘됨.

이미지 링크 : https://drive.google.com/drive/folders/1M72zZSTV4FuR-ve2gKfNIDsvtMk7CuaI?usp=sharing
이미지는 자신이 원하는 사진으로 바꿔도 가능하지만, img 딕셔너리의 value 값(파일 이름, 위치)을 바꿔줘야함.

