#!/usr/bin/env python
# coding: utf-8

# In[124]:


from pandas_datareader import data  
import pandas as pd
from datetime import datetime 
# 선택적으로 일정 기간동안의 주식 정보를 가져오는 방법입니다.


#  1.DataReader API를 통해서 yahoo finance의 주식 종목 데이터를 가져온다.

# In[125]:


df = data.DataReader("^KS11", "yahoo") 


# In[126]:


start_date = datetime(2019,1,1)
end_date = datetime(2020,12,10)


#  #고가, 저가, 시초가, 종가, 거래량, 수정 주가

# In[127]:


df


#  2.get_data_yahoo API를 통해서 yahho finance의 주식 종목 데이터를 가져온다.

# In[715]:


df = data.get_data_yahoo('^KS11')


# In[716]:


start = datetime(2020,2,17)
end = datetime(2020,12,12)


#  #시작날짜, 마지막 날짜 적용

# In[717]:


df= data.get_data_yahoo('^KS11',start,end)


# In[718]:


df

df['Close'].plot()
# In[719]:


df.plot()


# # 코스피open , close ,volume 기준 

# In[720]:


df_1=df[['Open','Close','Volume']]
df_1


# # 코스피 종가 기준 주가변동

# In[721]:


type(df['Close'])


# In[722]:


df_sample=df['Close']


# In[723]:


df['Close'].shift(1)  #어제 종가 칼럼: 정확히 말하면 이전 거래일의 종가를 의미, shift()함수는 데이터를 이동시킬 때 사용하는 함수로, 인수로 n을 줄 경우 전체 데이터가 n행씩 뒤로 이동한다.


# # 날짜별 코스피 주가 그래프로 나타내기 

# In[724]:


import matplotlib.pyplot as plt
plt.title('KOSPI',fontsize=16)
plt.ylabel('close',fontsize=11)
df_sample.plot()


# # 이 기간동안 제일 낮은 종가 날짜 상위 30일 꺼내기. 

# In[ ]:





# In[ ]:





# In[ ]:





# In[688]:


dataframe=pd.DataFrame(df)


# # 일간 변동률 구하기

# In[689]:


df_dpc=(df['Close']/df['Close'].shift(1)-1)*100 


# In[690]:


df_dpc.head()


# In[691]:


df_dpc.iloc[0]=0 #첫 번째 일간 변동률의 값이 NaN인데, 향후 계산을 위해서 NaN을 0으로 변경할 필요o
df_dpc


# In[692]:


plt.title('KOSPI fluctuation rate',fontsize=16)
plt.ylabel('daily fluctuation rate',fontsize=10)
df_dpc.plot()  


# In[693]:


print(df_dpc.columns)


# In[ ]:





# #  코로나확진자수
# 

# In[694]:


import requests
import json
import datetime as dt
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot
from IPython.display import SVG   # jupyter 상에서 SVG 이미지를 표시하기 위한 패키지
from bs4 import BeautifulSoup     # TAG로부터 원하는 내용을 추출하는 클래스 -> SVG 이미지의 핸 들링을 위함 
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
session = requests.Session()
session.headers.update( {'User-agent': user_agent, 'referer': None} )
api_url = "http://itpaper.co.kr/demo/covid19/all.php"


# In[695]:


r = session.get(api_url)

if r.status_code != 200:
    print("[%d Error] %s" % (r.status_code, r.reason))
    quit()

r.encoding = "utf-8"
covid19_dict = json.loads(r.text)


# In[696]:


지역명 = list(covid19_dict['data'].keys())
데이터누적 = DataFrame()

for v in 지역명:
    # 하나의 지역을 임시 데이터 프레임으로 변환
    tmp_df = DataFrame(covid19_dict['data'][v])
    
    # 임시 데이터 프레임에 지역명 컬럼 추가
    tmp_df['지역'] = v
    
    # 임시 데이터 프레임을 누적해서 병합
    데이터누적 = 데이터누적.append(tmp_df)

# 컬럼이름 변경을 위한 딕셔너리 정의
column_name = {'date': 'Date', 'active': '치료중', 'confirmed_acc': '누적확진자', 'death_acc': '누적사망자', 'released_acc': '누적격리해제', 'confirmed': '확진자', 'death': '사망자', 'released': '격리해제'}

데이터누적.rename(columns=column_name, inplace=True)

# 데이터 병합과정에서 중복되는 index가 발생하므로 index번호를 리셋한다.
# -> drop=True는 기존의 인덱스는 삭제하는 옵션
데이터누적.reset_index(drop=True, inplace=True)

데이터누적


# In[ ]:





# In[697]:


covid19_df = 데이터누적.copy()

for i in list(covid19_df.index):
    Date = covid19_df.loc[i, 'Date']
    p = Date.find(".")
    월 = int(Date[:p])
    일 = int(Date[p+1:])
    변환Date = "%04d/%02d/%02d" % (2020, 월, 일)
    #print(변환날짜)
    
    # 변환 결과를 다시 Dataframe에 넣는다.
    covid19_df.loc[i, 'Date'] = 변환Date
    
# 데이터프레임의 날짜 컬럼을 datetime 형식으로 일괄 변환
# -> infer_datetime_format=True 는 파이썬이 문자열의 날짜형식을 지능적으로 판단하여 format을 추측
covid19_df['Date'] = pd.to_datetime(covid19_df['Date'], infer_datetime_format=True)
covid19_df['Date']
last_date = covid19_df['Date'].max()


# In[698]:


last_df = covid19_df[(covid19_df['Date'] == last_date)]
last_df
df = covid19_df.filter(['Date','치료중','누적확진자','누적사망자','누적격리해제','확진자','사망자','격리해제']).groupby('Date').sum()
df


# In[ ]:





# ##  개수출력

# In[699]:


dfa= df.loc[:,['확진자']]
left=dfa
dfa


# # 날짜를 date로 변경

# In[700]:


dfa


# In[ ]:





#  #  MERGE Close

# In[701]:


right=df_sample


# In[702]:


fdf=pd.merge(left,right, left_index=True, right_index=True) 
fdf


#  #  MERGE Open,Close,Volume

# In[703]:


fdg=pd.merge(left,df_1, left_index=True, right_index=True) 
fdg


# In[704]:


import statsmodels.api as sm
import statsmodels.formula.api as smf
model = smf.ols(formula = 'Open','Close','Volume' ~ '확진자', data = fdg)
result = model.fit()
result.summary()


# In[ ]:





# # 상관관계 나타내기

# In[ ]:


fdf.head()


# In[ ]:


fdf[['확진자', 'Close']].corr(method='pearson')


# # 단순회귀분석

# In[ ]:


import statsmodels.api as sm
import statsmodels.formula.api as smf
model = smf.ols(formula = 'Close ~ 확진자', data = fdf)
result = model.fit()
result.summary()


# # 이 회귀모형 식은 Y= 2087.0206+0.7808*'확진자수'
# ### 확진자 수가 1명 높아질수록 총 Colse 주가는 약 0.7808원 증가한다는 뜻. 
# ### 2월부터 ~ 12월까지 코로나 확진자수의 증가는 종가에 큰 영향을 미치지 않는다 

# ## 한글폰트 사용을 위해 

# In[ ]:


plt.rc('font',family="Malgun Gothic")


# In[ ]:





# # @seaborn라이브러리를 통해                                                            x축은 확진자 y축은 Close로 시각화자료 

# In[705]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x='확진자', y='Close', color='r', alpha=0.2, data=fdf)
plt.show()


# In[706]:


sns.regplot(x='확진자', y='Close', color='g', data=fdf, fit_reg=True)
plt.ylim( 1400, 2800)
plt.show()


# In[ ]:


#Shift+tab키 누르면 문서를 볼 수 있다.#lmplot과 regplt차이는 hue사용할 수 있냐 없냐 차이.
sns.lmplot(x='확진자', y='Close', data=fdf,ci=95) #95%신뢰구간 나타냄
plt.xlim(0,100)
plt.show()


# In[ ]:





# In[ ]:


sns.heatmap(data = fdf.corr(), annot=True, 
fmt = '.2f', linewidths=.5, cmap='Blues')


# In[ ]:





# In[ ]:





# # 코로나 확진자수와 종가 주가가 시간이 지남에 따라 상관관계가 적어지고 있는 것 아닐까?

# In[ ]:


pd.set_option('display.max_rows',200)
fdf.sort_values(by="Close", ascending=True, kind='quicksort')[:100]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




