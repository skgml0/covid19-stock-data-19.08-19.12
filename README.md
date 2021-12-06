# covid19-stock-data-19.08-19.12
빅데이터 강의. 코로나19확진자 수에 따른 주가 관계분석

# 목표 (Data Mining)
 빅데이터 수업에서 진행한 개인 자율 프로젝트로, 당시 이슈였던 주가와 코로나19 확진자 수의 관계에 대한 분석을 목표로 하였습니다.
 전체 기간동안 코로나 확진자 수와 코스피의 상관관계를 분석& 월별 상관관계 분석 
 
 다음의 가설 확인
  1. 코로나 19 확진자 수가 증가하면, 코스피 주가의 하락이 일어난다.
  
  >일일 확진자 수가 코스피 지수를 하락하게 하지않을까?
  
  2. 시간이 지나면서 비슷한 확진자 수일 경우 사람들의 투자심리가 무뎌져 코스피가 상승하는지? >월별로 상관관계의 차이
 
 <추가 목표>
  월간 변동률이 비슷한 종목을 클러스터링으로 묶어 코로나19확진자수 증가에 따라 +/0/- 로 묶여지는 비슷한 종목을 확인할 수 있다.
  
# 기간
 2020.11월 ~2020.12월
 
# 환경
- jupyter notebook
- pycharm
- Maria DB

# 이미지
  ![image](https://user-images.githubusercontent.com/52391780/144812550-fcd97cd1-de69-4b1a-a109-74755f55c10d.png)
 
 - 확진자 추이 그래프
 
  ![image](https://user-images.githubusercontent.com/52391780/144812610-84cbf466-2ea1-4f64-8e94-1e02197051b5.png)
  
 - 회귀 분석
  
  ![image](https://user-images.githubusercontent.com/52391780/144812807-bf21b711-dfd1-4646-a723-81ae407f3816.png)

 - 개선점 
 
  ![image](https://user-images.githubusercontent.com/52391780/144812904-58db7ea5-7a59-4186-a6db-508dd9a635df.png)
 
 - DB 세팅
 
 - ![image](https://user-images.githubusercontent.com/52391780/144812998-63a40eba-e8ef-49b0-a806-ced6e256c700.png)
 - ![image](https://user-images.githubusercontent.com/52391780/144813026-513526ad-424c-48e1-bfab-687a7717ae99.png)
 - ![image](https://user-images.githubusercontent.com/52391780/144813058-5f0a7c9d-7a1d-41df-8bbd-6222933e2aa3.png)
  
 - DB 주가 저장
 - ![image](https://user-images.githubusercontent.com/52391780/144813106-6c6a77a2-073e-4c8f-8437-ab5247787e46.png)
 
 - 주식 종목 분류
  ![image](https://user-images.githubusercontent.com/52391780/144813185-cc519107-d833-4d21-8eb7-b7aeaa9dae45.png)
 
 - 결과
 ![image](https://user-images.githubusercontent.com/52391780/144813511-f231b753-791c-4c38-87a8-cdd24b786cf8.png)


# 보완해야할 점
 추가 목표 : 산업 분류 별 월간 지수 변화율을 보여주고, 클러스터링으로 묶어서 코로나 확진자 증가에도 + / 0/ -타격을 받는 군집형성
 이를 위한 필요 작업
1. 해당 일별로 코스피 200 종목 안에서 산업분류21개 sector로 분류 작업
 
2. 산업분류 별 종목의 일일변화율 평균을 계산해야하는데, 이게 종목의 시총을 고려하지 않고 그냥 Average로 계산하면 안될것 같아 수식 정립에 어려움을 
 느낌
 
3.산업별 일별 변화율을 월별 변화율로 바꾸는 작업
 
my idea)  대안으로 산업분야 별 시총 1위 회사 종목으로 대표하면 ? 
> 그 회사의 외부요인 이벤트로 일일 변화율이 달라질 수 있기 때문에 전체를 대표한다고 볼 수 없을 것 같다.
