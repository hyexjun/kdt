from django.shortcuts import redirect, render
from board.models import Board
from django.db.models import Q 
from django.core.paginator import Paginator

# Create your views here.

#게시판리스트
def blist(request):
    nowpage = int(request.GET.get('nowpage',1))
    
    if request.method == 'GET':
        
        qs = Board.objects.all().order_by('-b_no')
        context={'blist':qs}
    else:
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        # title검색
        if category == 'title':
            qs = Board.objects.filter(b_title__contains=searchword)
            
        elif category == 'content':    
            qs = Board.objects.filter(b_content__contains=searchword)
            
        elif category == 'all':
            qs = Board.objects.filter(Q(b_content__contains=searchword)|Q(b_title__contains=searchword))
        
    #모든게시글 받아서 페이지 분기    
    paginator = Paginator(qs,10)    #10개씩 쪼개서 페이지를 나누겠음 30개면 paginator에는 1,2,3
    page = int(request.GET.get('nowpage',1))  #현재페이지 받음, 없을때 1고정, 1안쓰면 none으로 받음
    blist = paginator.get_page(nowpage) #그 페이지마다의 게시글들, 
    if request.method=='GET':
        context={'blist':blist, 'nowpage':nowpage}
    else:
        context={'blist':blist, 'nowpage':nowpage,'category':category,'searchword':searchword}
    
    return render(request,'blist.html',context)         
    
        


#게시판 글쓰기 페이지 열기
def bwrite(request):
    return render(request, 'write_view.html')

#게시판 글쓰고 db에 저장

def bwriteOk(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # qs = Board(b_id=id, b_title=title, b_content=content)
    # qs.save()
    
    Board.objects.create(b_id=id, b_title=title, b_content=content)
    
    return redirect('/board/blist')

def bview(request,b_no):
    qs = Board.objects.get(b_no=b_no)
    qs.b_hit = qs.b_hit+1
    qs.save()
    context = {'board':qs}
    return render(request, 'bview.html', context)


#수정누르면 창 보여주기
def bmodify(request,b_no):
    qs = Board.objects.get(b_no=b_no)
    context = {'board':qs}
    return render(request, 'bmodify.html', context)

#수정완료 후 db에 저장
def bmodifyOk(request):
    b_no = request.POST.get('b_no')
    title = request.POST.get('b_title')
    content = request.POST.get('b_content')
    
    qs = Board.objects.get(b_no=b_no)    #수정할 데이터를 찾아서
    qs.b_title=title                   
    qs.b_content=content
    qs.save()
    
    return render(request, 'bview.html',{"board":qs})

    
def bdelete(request,b_no):
    qs = Board.objects.get(b_no=b_no)
    qs.delete()
    
    return redirect('/board/blist')
 
       
    