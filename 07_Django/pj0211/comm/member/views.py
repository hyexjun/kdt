from django.shortcuts import redirect, render
from member.models import Member

# 로그인 클릭이 두 곳에 있고 한가지 함수로 경우를 나눠서 사용하니까
def login(req):     # 그냥 메인페이지에서 로그인메뉴 누를때는 get방식으로 들어올때, 찐로그인이 post방식

    if req.method == 'GET':
        return render(req, 'login.html')
    
    elif req.method == 'POST':   # else로 하면 안된다. get 외의 나머지가 post만 잇는게 아니라서;;
        inputId = req.POST.get('inputId')  # 인풋박스id의 네임=inputId를 겟해서 요기의 inputId로 재명명
        inputPw = req.POST.get('inputPw')  # 이하 동일

        try :
            qs = Member.objects.get(u_id=inputId, u_pw=inputPw)
        except Member.DoesNotExist :    # 이거 양식? 문법은 걍 외워라..
            # 멤버모델에서 존재하지 않는 경우를 예외처리 할 건데
            qs = None    # '없다'는 정보를 정해줘야함.. 정보 자체가 null이면 에러난다..

        # 15번줄 통과했단 것 자체가 DB에 있는 것과 매칭되는 id, pw가 있다는 뜻
        # 요 줄까지 qs는 일단 멤버 DB 덩어리 그 자체
        if qs :  # 그렇게 매칭되어 저 처리과정을 거친 qs값이 있으면
            # s_id = qs.u_id    # qs덩어리 중 u_id를 s_id라고 트리밍한 셈
            # req.session['s_id'] = s_id  # 근데 이거 'req.session['s_id'] = qs.u_id'라고 하면 안되나? == 돼요..
            req.session['s_id'] = qs.u_id
            req.session['s_name'] = qs.u_name
            return render(req, 'index.html')

        else :
            context = {'msg':'일치하는 회원 정보가 없습니다. 다시 시도해주세요.'}
            return render(req, 'login.html', context)

def logout(req):
    if req.session.get('s_id'):
        req.session.clear()
    
    return redirect('/')