import csv
from django.http import JsonResponse
from django.shortcuts import render
import requests
import json
import xmltodict
from fin.models import dailycovid , dailyvaccine
import pandas as pd 
import matplotlib.pyplot as plt
import pandas as pd
import FinanceDataReader as fdr
from dateutil.parser import parse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd
import FinanceDataReader as fdr
from dateutil.parser import parse
import datetime



def chart(request):
    # covidData()
    # vaccineData()
    
    return render(request, 'fview.html')

def pluspercent(ticker,toDate):
    # 코로나가 있던 2년을 기준으로 주식 정보를 가져온다.
    df = fdr.DataReader(ticker,'2020-01-01', '2022-01-19')
    df.reset_index(inplace=True)
    
    covid = dailycovid.objects.all().values().order_by('intdate')
    covid = pd.DataFrame(covid)
    covid.columns = ['strdate', 'intdate','deathCnt', 'decideCnt']
    covid['datetype']= pd.to_datetime(covid['intdate'], format="%Y%m%d")
    # 오늘 누적 확진자 - 어제 누적 확진자(diff())-> 하루 확진다, 값이 없을 경우 0으로 대체
    covid['dailydecide']=covid['decideCnt'].diff().fillna(0)
    # (다음행 - 현재행)÷현재행
    covid['dailydiff']=covid['dailydecide'].pct_change().fillna(0)
    
    # 그 결과를 새로운 변수에 할당
    todayBool = covid['intdate'] == int(toDate)
    yesBool = covid['intdate'] == int(toDate)-1
    # 조건를 충족하는 데이터를 필터링하여 새로운 변수에 저장
    toCnt = int(covid[todayBool]['dailydecide'])
    yesCnt = int(covid[yesBool]['dailydecide'])
    # 전일 대비 확진자 증가률
    covidrate = round((toCnt - yesCnt)/yesCnt,2)*100
    # 전일 대비 확진자 증가률 / 어제, 소수 1재자리 올림 > 10% 단위
    changePerceil = (np.ceil((toCnt - yesCnt)/yesCnt*10)/10)
    # 전일 대비 확진자 증가률 / 어제, 소수 1재자리 내림 > 10% 단위
    changePerfloor = (np.floor((toCnt - yesCnt)/yesCnt*10)/10)

    # 전일 대비 확진자 증가률를 10%의 단위로 
    covid["pluspercent"] = covid['dailydiff'].ge(changePerfloor) & covid['dailydiff'].lt(changePerceil)
    # 입력한 날짜의 확진자 증가률과 일치하는지 bool 형식으로 변환 후 True row 만 가져오기
    covidTrue= covid[covid["pluspercent"]] 
    # 가져온 row의 날짜와 일치하는 날짜들 bool 형식으로 변환
    isinDate = df['Date'].isin(covidTrue['datetype']) 
    # 해당 날짜들의 주식 정보 가져오기
    allData = df.loc[isinDate]
    # allData의 Date열의 값을 리스트로 저장
    Date = allData['Date'].values.tolist()
    allData['Change'] = allData['Change']*100
    Change = allData['Change'].values.tolist()
    # 그 중 Change 가져오기
    allChange = df.loc[isinDate]['Change']
    # Change 중 + 가져오기
    plusChange = df.loc[isinDate]['Change']>0
    rate = round(len(plusChange[plusChange])/len(allChange)*100,2)
    datetype= covidTrue['datetype'].values.tolist()
    dailydecide = covidTrue['dailydecide'].values.tolist()
    
    context = {'rate':rate,'covidrate':covidrate, 'changePerfloor':changePerfloor, "changePerceil":changePerceil, 'Date':Date, 'Change':Change , 'datetype':datetype,'dailydecide':dailydecide}
    return context
    

def etf(ticker):
    df = fdr.DataReader(ticker,'2020-01-01', '2022-01-19')
    df.reset_index(inplace=True)
    df['percent']=df['Close']/df.iloc[0,1]*100
    df['changeRation']=df['Change']*100
    return df

def covidgoingon(date):    #코로나 누적 확진자율, #코로나 증가 세기
    #인자로는 날짜만
    covid = dailycovid.objects.all().values().order_by('intdate')
    covid = pd.DataFrame(covid)
    covid.columns = ['strdate', 'intdate','deathCnt', 'decideCnt']
    # 오늘 누적 확진자 - 어제 누적 확진자(diff())-> 하루 확진다, 값이 없을 경우 0으로 대체
    covid['dailydecide']=covid['decideCnt'].diff().fillna(0)
    
    # 입력 받은 날 구하기
    todayCovid = covid['intdate'] == int(date)
    # 7일의 확진자 합을 넣을 변수 설정
    sevenCnt = 0
    # 7일 간의 확진자 숫자를 구하기
    for i in range(1,8):
        # 자동 변수 생성
        globals()['covid_'+str(i)] = covid['intdate'] == int(date) - i # 하루 전부터 7일 전까지
        globals()['covidCnt_'+str(i)] = int(covid[globals()[f'covid_{i}']]['decideCnt']) # 해당하는 날짜의 확진자 할당
        sevenCnt += globals()['covidCnt_'+str(i)] # 해당 값을 sevenCnt에 +
    sevenMean = sevenCnt/7
    # 조건를 충족하는 데이터를 필터링하여 새로운 변수에 저장
    tocovidCnt = int(covid[todayCovid]['decideCnt'])
    # 전국의 누적 확진자 %
    tocovidPer = round(int(covid[todayCovid]['decideCnt'])/50000000*100,2)
    covidCompare = round((tocovidCnt - sevenMean)/sevenMean*100,2)
    context = {'tocovidPer':tocovidPer,'covidCompare':covidCompare}
    return context

#종목 기준으로
#언제 최저점? = 언제 반등?
def lowpointday(ticker):
    df = fdr.DataReader(ticker,'2020-01-01', '2022-01-19')
    df.reset_index(inplace=True)
    #close 값이 제일 낮은 row의 date 구하기
    lowdayindex= df['Close'].argmin()
    lowday = df.loc[lowdayindex]['Date']
    
    c= ticker
    a= " 종목이 코로나 진행 기간 동안 최저점을 찍은 날짜는 "
    b= "입니다.   <br> "
    
    result=""
    result= c+ a+ str(lowday)[0:10]+ b

    return result


#얼마나 하락 ?
def lowration(ticker):
    df = fdr.DataReader(ticker,'2020-01-01', '2022-01-19')
    df.reset_index(inplace=True)
    lowdayindex= df['Close'].argmin()
    df['percent']=df['Close']/df.iloc[0,1]*100
    lowration = df.loc[lowdayindex]['percent']
    
    lowration2 = round(lowration,2)
    
    result=""
    a= "코로나 발생 이전인 2020년 1월 1일을 기준으로 하였을 때, 해당 날의 하락율은 -"
    b= str(round(100-lowration2, 2))
    c= "% 입니다.   <br>"
    result= a+b+c
    
    return result   #가장 하락한 날의, 처음 1월1일 기준으로의 등락율
    # return '3'   #가장 하락한 날의, 처음 1월1일 기준으로의 등락율
# print('1월1일 기점으로, 코로나 2년동안 가장 하락한 날의 등락율은 -', 100-lowration('069500'), '%')


#언제 최고점?
def highpointday(ticker):
    df = fdr.DataReader(ticker,'2020-01-01', '2022-01-19')
    df.reset_index(inplace=True)
    #close 값이 제일 낮은 row의 date 구하기
    highdayindex= df['Close'].argmax()
    highday = df.loc[highdayindex]['Date']
    
    
    result=""
    a= "해당 종목이 코로나 진행 기간 동안 최고점을 찍은 날짜는 "
    b= "입니다.   <br> "
    
    str(highday)[0:10] 
    result= a + str(highday)[0:10] + b 
    

    return result
    #이 결과값으로 나온 날을 활용해서 코로나 관련 데이터 가져오기.
# print('코로나 2년 동안 최고점을 찍은 날은', highpointday('069500'))


#얼마나 상승?
def highration(ticker):
    df = fdr.DataReader(ticker,'2020-01-01', '2022-01-19')
    df.reset_index(inplace=True)
    highdayindex= df['Close'].argmax()
    df['percent']=df['Close']/df.iloc[0,1]*100
    highration = df.loc[highdayindex]['percent']
    
    result=""
    a= "기준일과 비교했을 때 최고점 날의 상승률은 + "
    
    c= "% 입니다.   <br>"
    result= a+ str(  round(highration-100,2)) + c
    return result
    
    #가장 하락한 날의, 처음 1월1일 기준으로의 등락율
# print('1월1일 기점으로, 코로나 2년동안 가장 상승한 날의 상승율은 +', highration('069500')-100, '%')



# 언제 oo과 크로스?
def cross(ticker1, ticker2, startday, endday):
    df1 = fdr.DataReader(ticker1,startday, endday)
    df2 = fdr.DataReader(ticker2,startday, endday)
    
    df1['percent']=df1['Close']/df1.iloc[0,1]*100
    df2['percent']=df2['Close']/df2.iloc[0,1]*100
#df1의 percent컬럼과 df2의 percent컬럼 비교.
    df1['compare'] = df1['percent'] >= df2['percent']  #df1 가 df2보다 상승일 때
    df1higher= df1[df1['compare']]['Close'].count()
    allday=df1['Close'].count()
    df1higherpercent= df1higher/allday*100
    
    return df1higherpercent.round(2)

def fview(request):
    qs = dailycovid.objects.all().values().order_by('intdate')
    # print(qs)
    return render(request, 'fview.html')



def DailyCovid(request):
    covid = dailycovid.objects.all().values().order_by('intdate')  #covid db 다 불러와서
    covid = pd.DataFrame(covid)
    covid.columns = ['strdate', 'intdate','deathCnt', 'decideCnt']
    # 앞의 것과의 차이 앞에 없을 경우 0
    covid['dailydecide']=covid['decideCnt'].diff().fillna(0)   #covid 일일 신규 확진자 만들고
    intdate = covid['intdate'].values.tolist()
    dailydecide = covid['dailydecide'].values.tolist()
    context = {'intdate':intdate,'dailydecide':dailydecide}  #context에 태워보냄
    return JsonResponse(context)

def TotalCovid(request):
    covid = dailycovid.objects.all().values().order_by('intdate')
    covid = pd.DataFrame(covid)
    covid.columns = ['strdate', 'intdate','deathCnt', 'decideCnt']
    intdate = covid['intdate'].values.tolist()
    decideCnt = covid['decideCnt'].values.tolist()
    context = {'intdate':intdate,'decideCnt':decideCnt}
    return JsonResponse(context)

def DailyVaccine(request):
    vaccine = dailyvaccine.objects.all().values().order_by('intdate')
    vaccine = pd.DataFrame(vaccine)
    vaccine.columns = ['strdate', 'intdate', 'firstCnt', 'secondCnt', 'thirdCnt', 'totalFirstCnt', 'totalSecondCnt', 'totalThirdCnt']
    intdate = vaccine['intdate'].values.tolist()
    firstCnt = vaccine['firstCnt'].values.tolist()
    secondCnt = vaccine['secondCnt'].values.tolist()
    thirdCnt = vaccine['thirdCnt'].values.tolist()
    context = {'intdate':intdate, 'firstCnt':firstCnt, 'secondCnt':secondCnt, 'thirdCnt': thirdCnt}
    return JsonResponse(context)

def TotalVaccine(request):
    vaccine = dailyvaccine.objects.all().values().order_by('intdate')
    vaccine = pd.DataFrame(vaccine)
    vaccine.columns = ['strdate', 'intdate', 'firstCnt', 'secondCnt', 'thirdCnt', 'totalFirstCnt', 'totalSecondCnt', 'totalThirdCnt']
    intdate = vaccine['intdate'].values.tolist()
    totalFirstCnt = vaccine['totalFirstCnt'].values.tolist()
    totalSecondCnt = vaccine['totalSecondCnt'].values.tolist()
    totalThirdCnt = vaccine['totalThirdCnt'].values.tolist()
    context = {'intdate':intdate, 'totalFirstCnt':totalFirstCnt, 'totalSecondCnt':totalSecondCnt, 'totalThirdCnt': totalThirdCnt}
    return JsonResponse(context)

    
def code_DailyCovid(request):
    # ajax으로 받아온 code
    code = request.GET.get('code')
    codedata = fdr.DataReader(code,'2020-01-01', '2022-01-19')
    codedata = codedata.resample('D').first() # 빈 날짜 채워주기
    codedata = codedata.fillna(method= 'ffill') # NaN 값을 앞의 값으로 채우기
    codedata['percent']=codedata['Close']/codedata.iloc[0,1]*100  # 2020-01-01의 종가를 기준으로 비율
    codedata.reset_index(inplace=True) # indes 제거
    codeclose = codedata['percent'].values.tolist() # DataFrame의 percent 열의 값들을 리스트로
    covid = dailycovid.objects.all().values().order_by('intdate') #db에서 covid values 가져오기
    covid = pd.DataFrame(covid) # 가져온 값들을 DataFrame
    covid.columns = ['strdate', 'intdate','deathCnt', 'decideCnt'] # 각각의 columns 에 이름 부여
    intdate = covid['intdate'].values.tolist() # DataFrame의 intdate 열의 값들을 리스트로
    covid['dailydecide']=covid['decideCnt'].diff().fillna(0)
    dailydecide = covid['dailydecide'].values.tolist()
    lowpoint = lowpointday(code) # 언제 최저점?
    lowrate = lowration(code) #얼마나 하락 ?
    highpoint = highpointday(code) #언제 최고점?
    highrate = highration(code) # 얼마나 상승 ?
    context = {'codeclose':codeclose, 'intdate':intdate, 'dailydecide':dailydecide, 'lowpoint':lowpoint \
        ,'lowrate':lowrate, 'highpoint':highpoint, 'highrate':highrate}
    return JsonResponse(context)

def code_totalCovid(request):
    # ajax으로 받아온 code
    code = request.GET.get('code')
    codedata = fdr.DataReader(code,'2020-01-01', '2022-01-19')
    codedata = codedata.resample('D').first() # 빈 날짜 채워주기
    codedata = codedata.fillna(method= 'ffill') # NaN 값을 앞의 값으로 채우기
    codedata['percent']=codedata['Close']/codedata.iloc[0,1]*100 # 2020-01-01의 종가를 기준으로 비율
    codedata.reset_index(inplace=True) 
    codeclose = codedata['percent'].values.tolist()
    covid = dailycovid.objects.all().values().order_by('intdate')
    covid = pd.DataFrame(covid)
    covid.columns = ['strdate', 'intdate','deathCnt', 'decideCnt']
    intdate = covid['intdate'].values.tolist()
    decideCnt = covid['decideCnt'].values.tolist()
    lowpoint = lowpointday(code) # 언제 최저점?
    lowrate = lowration(code) #얼마나 하락 ?
    highpoint = highpointday(code) #언제 최고점?
    highrate = highration(code) # 얼마나 상승 ?
    context = {'codeclose':codeclose, 'intdate':intdate, 'decideCnt':decideCnt, 'lowpoint':lowpoint \
        ,'lowrate':lowrate, 'highpoint':highpoint, 'highrate':highrate}
    return JsonResponse(context)

def code_dailyVaccine(request):
    # ajax으로 받아온 code
    code = request.GET.get('code')
    codedata = fdr.DataReader(code,'2020-01-01', '2022-01-19')
    codedata = codedata.resample('D').first() # 빈 날짜 채워주기
    codedata = codedata.fillna(method= 'ffill') # NaN 값을 앞의 값으로 채우기
    codedata['percent']=codedata['Close']/codedata.iloc[0,1]*100
    codedata.reset_index(inplace=True)
    codeclose = codedata['percent'].values.tolist()
    vaccine = dailyvaccine.objects.all().values().order_by('intdate')
    vaccine = pd.DataFrame(vaccine)
    vaccine.columns = ['strdate', 'intdate', 'firstCnt', 'secondCnt', 'thirdCnt', 'totalFirstCnt', 'totalSecondCnt', 'totalThirdCnt']
    intdate = vaccine['intdate'].values.tolist()
    firstCnt = vaccine['firstCnt'].values.tolist()
    secondCnt = vaccine['secondCnt'].values.tolist()
    thirdCnt = vaccine['thirdCnt'].values.tolist()
    
    lowpoint = lowpointday(code) # 언제 최저점?
    lowrate = lowration(code) #얼마나 하락 ?
    highpoint = highpointday(code) #언제 최고점?
    highrate = highration(code) # 얼마나 상승 ?
    context = {'codeclose':codeclose, 'intdate':intdate, 'firstCnt':firstCnt, 'secondCnt':secondCnt, 'thirdCnt': thirdCnt, 'lowpoint':lowpoint \
        ,'lowrate':lowrate, 'highpoint':highpoint, 'highrate':highrate}
   
    return JsonResponse(context)

def code_totalVaccine(request):
    # ajax으로 받아온 code
    code = request.GET.get('code')
    codedata = fdr.DataReader(code,'2020-01-01', '2022-01-19')
    codedata = codedata.resample('D').first() # 빈 날짜 채워주기
    codedata = codedata.fillna(method= 'ffill') # NaN 값을 앞의 값으로 채우기
    codedata['percent']=codedata['Close']/codedata.iloc[0,1]*100
    codedata.reset_index(inplace=True)
    codeclose = codedata['percent'].values.tolist()
    vaccine = dailyvaccine.objects.all().values().order_by('intdate')
    vaccine = pd.DataFrame(vaccine)
    vaccine.columns = ['strdate', 'intdate', 'firstCnt', 'secondCnt', 'thirdCnt', 'totalFirstCnt', 'totalSecondCnt', 'totalThirdCnt']
    intdate = vaccine['intdate'].values.tolist()
    totalFirstCnt = vaccine['totalFirstCnt'].values.tolist()
    totalSecondCnt = vaccine['totalSecondCnt'].values.tolist()
    totalThirdCnt = vaccine['totalThirdCnt'].values.tolist()
    
    lowpoint = lowpointday(code) # 언제 최저점?
    lowrate = lowration(code) #얼마나 하락 ?
    highpoint = highpointday(code) #언제 최고점?
    highrate = highration(code) # 얼마나 상승 ?
    context = {'codeclose':codeclose, 'intdate':intdate,'totalFirstCnt':totalFirstCnt, 'totalSecondCnt':totalSecondCnt, 'totalThirdCnt': totalThirdCnt, 'lowpoint':lowpoint \
        ,'lowrate':lowrate, 'highpoint':highpoint, 'highrate':highrate}

    return JsonResponse(context)

def codeDate(request):
    code = request.GET.get('code')
    date = request.GET.get('date')
    percent = pluspercent(code, date)
    context = {'msg':'메세지 성공', 'percent':percent}
    return JsonResponse(context)

def covidspread(request):
    date = request.GET.get('date')
    spread = covidgoingon(date)
    print(spread)
    context = {'spread':spread}
    return JsonResponse(context)

def covidData():
    #수찬꺼 url
    url='http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=JvU2PSq9lh1mHsrlM5p7uq9GeNuR4KrBvrHcZO0jIb7unq5lANtM0HkaDA35GqYh3vhuWTXxlWrXqE8AZiqVSA%3D%3D&pageNo=1&numOfRows=1000&startCreateDt=20200120&endCreateDt=20220119'
    
    
    response= requests.get(url)
    contents=response.text    #받아온 텍스트는 xml 형식.
    dictionary = xmltodict.parse(contents)   # xml을 dic형식으로 만들고
    json_str= json.dumps(dictionary)   #dic을 json 형식으로 만들었는데 이러면 json str타입이 나옴.
    json_ob= json.loads(json_str)   # json str을 다시 json dict 객체로 만듦.
    covidData= json_ob['response']['body']['items']['item'] #해당 키 내의 벨류값 찾아옴

    # filename='확진 및 사망자.csv'
    # f= open(filename, 'w', encoding='utf-8-sig', newline='')
    # writer= csv.writer(f)
    # title= "date, intdate, deathCnt, decideCnt".split(',')
    # writer.writerow(title)

    for i in covidData:
        # rowdata=[]
        date= i['stateDt']
        deathCnt= i['deathCnt']
        decideCnt= i['decideCnt']
        qs = dailycovid(strdate=date,intdate=int(date), deathCnt=int(deathCnt), decideCnt=int(decideCnt))
        qs.save()
    # rowdata.append(date)
    # rowdata.append(int(date))
    # rowdata.append(deathCnt)
    # rowdata.append(decideCnt)
    # writer.writerow(rowdata)

def vaccineData():
    service_key = 'JvU2PSq9lh1mHsrlM5p7uq9GeNuR4KrBvrHcZO0jIb7unq5lANtM0HkaDA35GqYh3vhuWTXxlWrXqE8AZiqVSA%3D%3D'
    # filename = '백신 접종.csv'
    # f= open(filename, 'w', encoding='utf-8-sig', newline = '')
    # writer = csv.writer(f)
    # title = "date,firstCnt,secondCnt,thirdCnt,totalFirstCnt,totalSecondCnt,totalThirdCnt".split(',')
    # writer.writerow(title) 
    vaccineData = [] # 전체 data 리스트(2중)
    for i in range(356):  #페이지 별로
        url = f'http://api.odcloud.kr/api/15077756/v1/vaccine-stat?page={i}&perPage=18&serviceKey={service_key}'
        res = requests.get(url)
        contents = res.json()
        data = [] # 날짜별로 data를 넣을 리스트
        for i in range(18):  #날짜 row 별로
            if contents['data'][i]['sido'] == '전국':
                data.append(contents['data'][i]['baseDate'][0:4]+contents['data'][i]['baseDate'][5:7]+contents['data'][i]['baseDate'][8:10])
                data.append(int(contents['data'][i]['baseDate'][0:4]+contents['data'][i]['baseDate'][5:7]+contents['data'][i]['baseDate'][8:10]))
                data.append(contents['data'][i]['firstCnt'])
                data.append(contents['data'][i]['secondCnt'])
                data.append(contents['data'][i]['thirdCnt'])
                data.append(contents['data'][i]['totalFirstCnt'])
                data.append(contents['data'][i]['totalSecondCnt'])
                data.append(contents['data'][i]['totalThirdCnt'])
        # writer.writerow(data)
        vaccineData.append(data)
        
    for i in vaccineData:  #날짜 row 별로
        date = i[0]
        intdate = i[1]
        firstCnt = i[2]
        secondCnt = i[3]
        thirdCnt = i[4]
        totalFirstCnt = i[5]
        totalSecondCnt = i[6]
        totalThirdCnt = i[7]
        qs = dailyvaccine(strdate = date, intdate = intdate, firstCnt = firstCnt, secondCnt = secondCnt, thirdCnt = thirdCnt\
            ,totalFirstCnt = totalFirstCnt,totalSecondCnt = totalSecondCnt,totalThirdCnt = totalThirdCnt )
        qs.save()