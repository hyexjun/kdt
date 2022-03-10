import requests

# res = requests.get('http://www.google.com')
res = requests.get('https://www.melon.com/')
print('응답코드 : ',res.status_code) #200정상 , 401 권한 없음, 404페이지없음, 500 서버 에러 

if res.status_code == 200:
    print("정상적인 코드 입니다.")
else :
    print('접근할 수 없습니다. 응답 코드 : ', res.status_code)
    res.raise_for_status() #정상코드가 아니면 프로그램 종료
    print('실행 확인')
    
    
# with open('01_google.html', 'w', encoding='utf-8') as f:
#     f.write(res.text)