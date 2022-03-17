import bs4
from django.shortcuts import render
import cx_Oracle as ora  # 오라클 연동
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from django.shortcuts import render, redirect
from urllib.request import Request, urlopen
from urllib.parse import urlencode, unquote, quote_plus
import json
import matplotlib
import xmltodict
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager, rc
import requests
from django.shortcuts import render
import requests
import json
import pandas as pd
from seoul.models import *

##########################################################################
#자치구별 확진자 현황 표에 데이터 뿌리기


def sview(req):
    # death()
    # patientsum()
    # patientadd()

    conn = ora.connect('ora_user/1234@localhost:1521/orcl')

    #구별누적확진자데이터
    qs = Patientsum.objects.all()
    object_df3 = pd.DataFrame.from_records(qs.values())
    #구별 일일 추가 확진자
    qs2 = Patientadd.objects.all()
    daily = pd.DataFrame.from_records(qs2.values())

    #전체/서울 신규.누적.사망자 데이터
    qs3 = Death.objects.all()
    totaldata = pd.DataFrame.from_records(qs3.values())

    #최신날짜로 정렬
    df = object_df3.sort_values(by=['date'], ascending=False)
    df2 = daily.sort_values(by=['date'], ascending=False)

    sumdata = []  # 현재까지 누적 구별 확진자 리스트로(마포구까지)
    sumdata2 = []  # 현재까지 누적 구별 확진자 리스트로(서대문구~중랑구)

    dailydata = []  # 구별 일일 추가 확진자 리스트로(마포구까지)
    dailydata2 = []  # 구별 일일 추가 확진자 리스트로(서대문구~중랑구)

    allcovid = []  # 전국 신규,누적,사망자
    seoulcovid = []  # 서울 신규,누적,사망자

    #날짜순으로 정렬했을 때 0행이 최신, 포문으로 컬럼값을 빈 리스트에 넣어서
    #html로 보내줌
    for i in range(13):
        gudata = format(df.iloc[0][i+1], ',')
        dailydatas = format(df2.iloc[0][i+1], ',')

        sumdata.append(gudata)
        dailydata.append(dailydatas)

    for i in range(12):
        gudata2 = format(df.iloc[0][i+14], ',')
        dailydatas2 = format(df2.iloc[0][i+14], ',')
        sumdata2.append(gudata2)
        dailydata2.append(dailydatas2)

    for i in range(3):
        alldata = format(totaldata.iloc[0][i+3], ',')
        allcovid.append(alldata)
        alldata2 = format(totaldata.iloc[1][i+3], ',')
        seoulcovid.append(alldata2)

    context = {'gudata': sumdata, 'gudata2': sumdata2, 'dailydata': dailydata,
               'dailydata2': dailydata2, 'alldata': allcovid, 'alldata2': seoulcovid}
    print(allcovid)
    return render(req, 'sview.html', context)
##########################################################################
#자치구별 확진자 추이div에 차트 그리기


def chartshow(request):
    qs2 = Patientadd.objects.all()
    daily = pd.DataFrame.from_records(qs2.values())
    df2 = daily.sort_values(by=['date'], ascending=False)

    dailyData = []
    #포문으로 전체 컬럼을 list로 담아서 html에 보내기
    for i in range(25):
        dailydatas = format(df2.iloc[0][i+1])  # format을 안씌워주면 TypeError가 뜸
        dailyData.append(dailydatas)
    print(dailydatas)
    context = {'dailydata': dailyData}
    return JsonResponse(context)


#############################################################################################
#오라클에 누적확진자 데이터 넣기

def patientsum(request):

    serial_key = "6453454b53746d6438337244774474"
    url = "http://openapi.seoul.go.kr:8088/{}/json/TbCorona19CountStatusJCG/1/800/".format(
        serial_key)
    response = requests.get(url)
    contents = response.text
    json_ob = json.loads(contents)
    publicData = json_ob["TbCorona19CountStatusJCG"]["row"]
    df = pd.json_normalize(publicData)

    df['DATETIME'] = pd.to_datetime(df['JCG_DT'])
    df['YEAR'] = df['DATETIME'].dt.year
    df['DATETIME'] = df['DATETIME'].dt.date
    df['DATETIME'] = df['DATETIME'].apply(lambda x: x.strftime('%Y-%m-%d'))
    mask = df["YEAR"].isin([2022, 2021, 2020])
    df = df[mask]
    df = df[:-3]

    df = df[["DATETIME", "GANGNAM", "GANGDONG", "GANGBUK", "GANGSEO", "GWANAK", "GWANGJIN", "GURO", "GEUMCHEON", "NOWON", "DOBONG", "DDM",
             "DONGJAK", "MAPO", "SDM", "SEOCHO", "SEONGDONG", "SEONGBUK", "SONGPA", "YANGCHEON", "YDP", "YONGSAN", "EP", "JONGNO", "JUNGGU", "JUNGNANG"]]

    rows = []
    for x in df.to_records(index=False):
        row = [x[0], int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]), int(x[6]), int(x[7]), int(x[8]), int(x[9]), int(x[10]), int(x[11]), int(x[12]), int(
            x[13]), int(x[14]), int(x[15]), int(x[16]), int(x[17]), int(x[18]), int(x[19]), int(x[20]), int(x[21]), int(x[22]), int(x[23]), int(x[24]), int(x[25])]
        # 전체 list에 담음.
        rows.append(row)

        date = row[0]
        gangnam = row[1]
        gangdong = row[2]
        gangbuk = row[3]
        gangseo = row[4]
        gwanak = row[5]
        gwangjin = row[6]
        guro = row[7]
        geumcheon = row[8]
        nowon = row[9]
        dobong = row[10]
        ddm = row[11]
        dongjak = row[12]
        mapo = row[13]
        sdm = row[14]
        seocho = row[15]
        seongdong = row[16]
        seongbuk = row[17]
        songpa = row[18]
        yangcheon = row[19]
        ydp = row[20]
        yongsan = row[21]
        ep = row[22]
        jongno = row[23]
        junggu = row[24]
        jungnang = row[25]

        qs = Patientsum(date=date, gangnam=gangnam, gangdong=gangdong, gangbuk=gangbuk, gangseo=gangseo,
                        gwanak=gwanak, gwangjin=gwangjin, guro=guro, geumcheon=geumcheon, nowon=nowon,
                        dobong=dobong, ddm=ddm, dongjak=dongjak, mapo=mapo, sdm=sdm, seocho=seocho,
                        seongdong=seongdong, seongbuk=seongbuk, songpa=songpa, yangcheon=yangcheon,
                        ydp=ydp, yongsan=yongsan, ep=ep, jongno=jongno, junggu=junggu, jungnang=jungnang)
        qs.save()

#############################################################################################
#오라클에 일일확진자 데이터 넣기


def patientadd(request):

    serial_key = "6453454b53746d6438337244774474"
    url = "http://openapi.seoul.go.kr:8088/{}/json/TbCorona19CountStatusJCG/1/800/".format(
        serial_key)
    response = requests.get(url)
    contents = response.text
    json_ob = json.loads(contents)
    publicData = json_ob["TbCorona19CountStatusJCG"]["row"]
    df = pd.json_normalize(publicData)

    df['DATETIME'] = pd.to_datetime(df['JCG_DT'])
    df['YEAR'] = df['DATETIME'].dt.year
    df['DATETIME'] = df['DATETIME'].dt.date
    df['DATETIME'] = df['DATETIME'].apply(lambda x: x.strftime('%Y-%m-%d'))
    mask = df["YEAR"].isin([2022, 2021, 2020])
    df = df[mask]
    df = df[:-3]

    df = df[["DATETIME", "GANGNAMADD", "GANGDONGADD", "GANGBUKADD", "GANGSEOADD", "GWANAKADD", "GWANGJINADD", "GUROADD", "GEUMCHEONADD", "NOWONADD", "DOBONGADD", "DDMADD", "DONGJAKADD",
             "MAPOADD", "SDMADD", "SEOCHOADD", "SEONGDONGADD", "SEONGBUKADD", "SONGPAADD", "YANGCHEONADD", "YDPADD", "YONGSANADD", "EPADD", "JONGNOADD", "JUNGGUADD", "JUNGNANGADD"]]

    rows = []
    for x in df.to_records(index=False):
        row = [x[0], int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]), int(x[6]), int(x[7]), int(x[8]), int(x[9]), int(x[10]), int(x[11]), int(x[12]), int(
            x[13]), int(x[14]), int(x[15]), int(x[16]), int(x[17]), int(x[18]), int(x[19]), int(x[20]), int(x[21]), int(x[22]), int(x[23]), int(x[24]), int(x[25])]
        # 전체 list에 담음.
        rows.append(row)

        date = row[0]
        gangnam = row[1]
        gangdong = row[2]
        gangbuk = row[3]
        gangseo = row[4]
        gwanak = row[5]
        gwangjin = row[6]
        guro = row[7]
        geumcheon = row[8]
        nowon = row[9]
        dobong = row[10]
        ddm = row[11]
        dongjak = row[12]
        mapo = row[13]
        sdm = row[14]
        seocho = row[15]
        seongdong = row[16]
        seongbuk = row[17]
        songpa = row[18]
        yangcheon = row[19]
        ydp = row[20]
        yongsan = row[21]
        ep = row[22]
        jongno = row[23]
        junggu = row[24]
        jungnang = row[25]

        qs = Patientadd(date=date, gangnam=gangnam, gangdong=gangdong, gangbuk=gangbuk, gangseo=gangseo,
                        gwanak=gwanak, gwangjin=gwangjin, guro=guro, geumcheon=geumcheon, nowon=nowon,
                        dobong=dobong, ddm=ddm, dongjak=dongjak, mapo=mapo, sdm=sdm, seocho=seocho,
                        seongdong=seongdong, seongbuk=seongbuk, songpa=songpa, yangcheon=yangcheon,
                        ydp=ydp, yongsan=yongsan, ep=ep, jongno=jongno, junggu=junggu, jungnang=jungnang)
        qs.save()
#############################################################################################

#서울시/전국 신규/누적/사망자 데이터 넣기


def death(request):

    day = datetime.datetime.now()
    days = day.strftime('%Y-%m-%d').replace("-", "")

    serial_key = 'tNZFWWXUaNeQrEFYg8kFCRh0AJ/Rj8w3jSaKrKIWclkI5NMy83X+gQvspPK1yMok7/FfAE9u+8ZAalPLQ7daFw=='
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'
    params = {'serviceKey': serial_key, 'pageNo': '1',
              'numOfRows': '10000', 'startCreateDt': days, 'endCreateDt': days}
    response = requests.get(url, params=params)
    contents = response.text
    xml_obj = bs4.BeautifulSoup(contents, 'lxml-xml')
    rows = xml_obj.findAll('item')
    row_list = []  # 행값
    name_list = []  # 열이름값
    value_list = []  # 데이터값
    data = []

    for i in range(0, len(rows)):
        columns = rows[i].find_all()
        #첫째 행 데이터 수집
        for j in range(0, len(columns)):
            if i == 0:
                # 컬럼 이름 값 저장
                name_list.append(columns[j].name)
            # 컬럼의 각 데이터 값 저장
            value_list.append(columns[j].text)
        # 각 행의 value값 전체 저장
        row_list.append(value_list)
        # 데이터 리스트 값 초기화
        value_list = []
    df = pd.DataFrame(row_list, columns=name_list)
    df = df.tail(2)
    df = df[::-1]

    df['DATETIME'] = pd.to_datetime(df['createDt'])
    df['DATETIME'] = df['DATETIME'].dt.date

    df = df[["DATETIME", "gubun", "deathCnt", "incDec", "defCnt"]]
    rows = []

    for x in df.to_records(index=False):
        row = [x[0], x[1], int(x[2]), int(x[3]), int(x[4])]

        date = row[0]
        location = row[1]
        deathcnt = row[2]
        incdec = row[3]
        defCnt = row[4]

        sd = Death(date=date, location=location,
                   deathcnt=deathcnt, incdec=incdec, defCnt=defCnt)
        sd.save()