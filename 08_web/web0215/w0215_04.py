import requests
from bs4 import BeautifulSoup


for year in range(2017, 2022) :
    url="https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
    res = requests.get(url,headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    # 1개 이미지 따오기 테스트
    img1 = soup.find("img", {"class":"thumb_img"})['src']


    imgs = soup.find_all("img", {"class":"thumb_img"})
    for idx, img in enumerate(imgs) :
        img_url = img['src']
        print(img_url)

        img_res = requests.get(img_url)
        img_res.raise_for_status()    # 동일하게 링크 가져올 게 없으면 종료하라는 뜻


        # "w"는 str 텍스트, "wb"는 바이너리 머시기?
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f :
            f.write(img_res.content)

        
        if (idx==4) :   # 이미지 5개 되면 종료
            break       # 이거 없으면 이 페이지 내 저 클래스 먹인 이미지 다 저장됨 55개..