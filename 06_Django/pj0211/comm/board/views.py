from django.shortcuts import redirect, render
from board.models import Board
from member.models import Member
from django.db.models import Max, Min, Avg


# Create your views here.
def blist(req):
    qs = Board.objects.all().order_by('-b_group', 'b_step')
    return render(req, 'blist.html')


def bwrite(req):
    return render(req, 'bwrite.html')


def bwriteOk(req):
    id = req.POST.get('id')
    member = Member.objects.get(u_name=id)
    # member = Member.objects.get(u_id=req.POST.get('id'))  # 15, 16번줄 합쳤음
    title = req.POST.get('title')      # 요 네 가지 항목 get('인풋박스의 name속성')
    content = req.POST.get('content')
    img = req.FILES.get('img', '')     # img가 없으면 공란으로 나와도 괜찮게 하는 ''빈칸처리? 였던거가틈
    # 여기까지는 글쓰기페이지에서 넘어오는 4종류 인풋데이터
    # 내가 지금 쓰는 글의 게시글번호.. 만들어줘야된다..
    no = Board.objects.aggregate(max_b_no=Max('b_no'))  # b_no최대수를 maxno라 명명
    # aggregate 관련 메소드 max, min, avg 등
    # 뭐 있긴 했는데 이거는 쓰는 양식 걍 외우자.. 컨트롤+쩜으로 import도 안 나오니까 걍 쳐라..
    # from django.db.models import Max, Min, Avg   <--- 이거 맨 윗줄 치면 된단다
    max_no = no['max_b_no']   # no[] 속에는 명사형만 들어와야된다고 함.. 그래서 25번줄 속에서 maxno 선언
    max_no += 1
    b_no = max_no

    qs = Board(b_no=b_no, member=member, b_title=title,
               b_content=content, b_group=b_no, b_img=img)
    qs.save()

    return redirect('board:blist')
