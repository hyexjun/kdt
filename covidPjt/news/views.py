from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.core.paginator import Paginator
from news.models import News, Comment
from django.db.models import Max,Min,Avg 
import requests
from bs4 import BeautifulSoup


def nlist(request):
    nowpage = request.GET.get('nowpage',1)
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    titles = soup.find_all("a",{"class":"news_tit"})
    subtitles = soup.find_all("a",{"class":"info press"})
    times = soup.find_all("span",{"class":"info"})
    imgs = soup.find_all("img",{"class":"thumb api_get"})
    
    
    publicData=[]
    for title in titles:
        name=title["title"]
        datalist={'title':name}
        publicData.append(datalist)
        
    for i,sub in enumerate(subtitles):
        subtitle=sub.get_text()
        data={'subtitle':subtitle}
        publicData[i].update(data)
        # datalist={'subtitle':subtitle}
    
    for i,time in enumerate(times):
        time1=time.get_text()
        data1={'time':time1}
        publicData[i].update(data1)
        
    for i,img in enumerate(imgs):
        img1=img['src']
        data2={'img':img1}
        publicData[i].update(data2)
        
    for i, href in enumerate(titles):
        href1=href['href']
        data4={'href':href1}
        publicData[i].update(data4)

    context={'publicData':publicData}
    return render(request,'nlist.html',context)