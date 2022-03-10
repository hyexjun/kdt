from django.shortcuts import redirect, render

from member.models import Member

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        #예외처리
        
        qs = Member.objects.get(m_id=id, m_pw=pw)
        if qs:
            session_id = qs.m_id
            request.session['session_id'] = session_id
        else:
            msg = "아이디와 패서워드가 일치하지 않습니다."
        
        
        return redirect('/')