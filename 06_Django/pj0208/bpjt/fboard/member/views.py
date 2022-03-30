from django.shortcuts import redirect, render
from member.models import Member

# Create your views here.
def login(req):
    return render(req, 'login.html')

def loginOk(req):
    id = req.POST.get('id')
    pw = req.POST.get('pw')

    # id, pw가 일치하지 않을 때 예외처리
    try :
        member = Member.objects.get(m_id=id, m_pw=pw)
    except Member.DoesNotExist :
        member = None

    # member의 id가 있으면
    if member :
        id = member.m_id
        name = member.m_name
        req.session['session_id'] = id  # {'session_id':'aaa'}
        req.session['session_name'] = name  # {'session_name':'name'}
        return redirect('/') 
    else :
        context = {'msg':'아이디와 패스워드가 일치하지 않습니다.'}
        return render(req,'login.html', context)

    

def logout(req):
    if req.session.get('session_id'):
        req.session.clear()               # 세션 전체 삭제
        # del req.session['session_id']   # 해당 세션 일부 삭제
    return redirect('/')