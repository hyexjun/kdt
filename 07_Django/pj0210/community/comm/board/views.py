import json
from django.shortcuts import redirect, render
from board.models import Board
from django.db.models import Q, F
from django.core.paginator import Paginator
from member.models import Member
from django.db.models import Max, Min, Avg 
import urllib        # 한글로 인코딩
import requests      # 웹스크롤링
import datetime

def notice(req):
    return render(req, 'customer/notice.html')

def notice_view(req):
    return render(req, 'customer/notice_view.html')




# 게시판리스트
def blist(request):
    # 현재페이지 받음, 없을때 1 고정
    nowpage = int(request.GET.get('nowpage', 1))      # 초록나우페이지 어디가 시작점임? 여기가 맞나요?
    
    # 이건 걍 메인페이지에서 게시판뷰 갔을 때 표시되는 용? 맞지요?ㅎ == 이건 카테고리를 안 건드린 상태, 자연상태
    if request.method == 'GET':
        
        qs = Board.objects.all().order_by('-b_group', 'b_step')    # 일단 페이지 데이터를 쭈루룩 받아서 행 쭈르륵ㅎ
        paginator = Paginator(qs, 10)                              # 그걸 10개씩 쪼개서 페이지화 할거예요?ㅎㅎ
        blist = paginator.get_page(nowpage)                        # 1,2,3 10개 blist에 담음
        context = {'blist':blist, 'nowpage':nowpage}
        return render(request, 'newblist.html', context)
    
    # 여기는 카테고리를 건드린, 검색 옵션을 설정한 상태
    else:
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        # title 검색
        if category == 'title':
            qs = Board.objects.filter(b_title__contains=searchword)
            paginator = Paginator(qs, 10)
            blist = paginator.get_page(nowpage)
            context = {'blist':blist, 'nowpage':nowpage, 'category':category, 'searchword':searchword}
            return render(request, 'blist.html', context)
            
        elif category == 'content':    
            qs = Board.objects.filter(b_content__contains=searchword)
            paginator = Paginator(qs, 10)
            blist = paginator.get_page(nowpage)
            context = {'blist':blist, 'nowpage':nowpage, 'category':category, 'searchword':searchword}
            return render(request, 'blist.html', context)
        
        elif category == 'all':
            # a and b
            # qs = Board.objects.filter(b_title__contains=searchword,b_content__contains=searchword)
            # a or b
            qs = Board.objects.filter(Q(b_title__contains=searchword)|Q(b_content__contains=searchword))
            paginator = Paginator(qs, 10)
            blist = paginator.get_page(nowpage)
            context = {'blist':blist, 'nowpage':nowpage, 'category':category, 'searchword':searchword}
            return render(request, 'blist.html', context)

# 뷰페이지
def bview(request, b_no):
    qs = Board.objects.get(b_no=b_no)
    qs.b_hit += 1
    qs.save()
    context = {'board':qs}
    return render(request, 'bview.html', context)

# 수정페이지
def bmodify(request, b_no):
    qs = Board.objects.get(b_no=b_no)
    context = {'board':qs}
    return render(request, 'bmodify.html', context)

# 수정페이지저장
def bmodifyOk(request):
    b_no = request.POST.get('b_no')
    b_title = request.POST.get('b_title')
    b_content = request.POST.get('b_content')
    # 파일이름 가져오기 
    b_img = request.FILES.get('b_img', '')
    print("views file : ", request.FILES)
    qs = Board.objects.get(b_no=b_no)
    qs.b_title = b_title
    qs.b_content = b_content
    # 파일이름 저장
    qs.b_img = b_img
    qs.save()
    # Board.objects.create(b_id=id,b_title=title,b_content=content)
    # context = {"board":qs}
    return render(request, 'bview.html', {"board":qs})
    # return redirect('board:bview')

# 게시판글쓰기
def bwrite(request):
    return render(request, 'bwrite.html')

# 게시판글쓰기저장
def bwriteOk(request):
    id = request.POST.get('id')
    member = Member.objects.get(m_id=id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    img = request.FILES.get('img', '')

    # b_no를 수동으로 1씩 증가해서 저장시켜줌
    no = Board.objects.aggregate(max_b_no=Max('b_no'))
    max_no = no['max_b_no']  # b_no 최대 번호 찾아오기
    max_no += 1         # 거기에다가 더 제일 큰 숫자를 만들어주기
    b_no = max_no

    qs = Board(b_no=b_no, member=member, b_title=title, b_content=content, b_group=b_no, b_img=img)
    qs.save()
    # Board.objects.create(b_id=id,b_title=title,b_content=content)
    return redirect('board:blist')

# 게시글 삭제
def bdelete(request, b_no):
    qs = Board.objects.get(b_no=b_no)
    qs.delete()
    return redirect('board:blist')

# 답글작성페이지로
def breply(request, b_no):
    qs = Board.objects.get(b_no=b_no)
    context = {'board':qs}

    return render(request, 'breply.html', context)

# 답글작성페이지에서 쓴 내용 저장, 전송
def breplyOk(request):

    # b_no를 수동으로 1씩 증가해서 저장시켜줌
    no = Board.objects.aggregate(max_b_no=Max('b_no'))
    max_no = no['max_b_no']  # b_no 최대 번호 찾아오기
    max_no += 1         # 거기에다가 더 제일 큰 숫자를 만들어주기
    b_no = max_no

    # 부모의 정보 가져와야됨
    # b_no = request.POST.get('b_no')
    b_group = int(request.POST.get('b_group'))
    b_step = int(request.POST.get('b_step'))
    b_indent = int(request.POST.get('b_indent'))

    # 답글의 내용
    id = request.POST.get('id')
    member = Member.objects.get(m_id=id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    img = request.FILES.get('img', '')


    Board.objects.filter(b_group=b_group, b_step__gt=b_step).update(b_step=F('b_step')+1)

    # 부모의 b_group, b_step+1, b_indent+1
    qs = Board(b_no=b_no, member=member, b_title=title, b_content=content, b_group=b_group, b_img=img, b_step=b_step+1, b_indent=b_indent+1)
    qs.save()
    # Board.objects.create(b_id=id,b_title=title,b_content=content)
    return redirect('board:blist')


def publicData(request):
    m_serviceKey = '9n%2B%2BK6qIyspgnyqIXXSYKpPfdZSxJhG4%2BIq2jImDo86ZVlG1kdKQLWU6txWwHBhDSBFPEe5yPCLiN%2BSyYgw6sw%3D%3D'
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryList?serviceKey={}&pageNo=1&numOfRows=10&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'.format(m_serviceKey)
    params ={'serviceKey' : m_serviceKey, 'pageNo' : '1', 'numOfRows' : '10', 'MobileOS' : 'ETC', 'MobileApp' : 'AppTest', 'arrange' : 'A' }
    response = requests.get(url, params=params)
    contents = response.text        # reponse의 내용을 텍스트화
    json_ob = json.loads(contents)  # 텍스트를 json 타입으로 변환
    publicData = json_ob['response']['body']['items']['item']   # json 데이터에서 쇽쇽쇽 층 들어가는 느낌
    context = {'publicData':publicData}

    return render(request, 'publicData.html', context)


def publicData2(request):
    nowpage = request.GET.get('nowpage', 1)
    m_serviceKey = '9n%2B%2BK6qIyspgnyqIXXSYKpPfdZSxJhG4%2BIq2jImDo86ZVlG1kdKQLWU6txWwHBhDSBFPEe5yPCLiN%2BSyYgw6sw%3D%3D'
    url = 'https://api.odcloud.kr/api/apnmOrg/v1/list?page={}&perPage=10&serviceKey={}'.format(nowpage, m_serviceKey)
    response = requests.get(url)
    contents = response.text
    json_ob = json.loads(contents)
    publicData2 = json_ob['data']
    context = {'publicData2':publicData2}

    return render(request, 'publicData2.html', context)