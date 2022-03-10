from django.http import JsonResponse
from django.shortcuts import redirect, render
from member.models import Member

# Create your views here.

def login(request):
    if request.method == 'GET':
        print("views get : login")
        return render(request, 'login.html')
    
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')


        try:
            qs = Member.objects.get(m_id=id, m_pw=pw)
        except Member.DoesNotExist:   # DB에 없는 아이디와 비번 입력 시
            qs = None                 # none으로 '없다는 것'을 정의하지 않으면 에러페이지 발생하므로 예외처리 
        

        if qs:
            s_id = qs.m_id
            request.session['s_id'] = s_id
            return render(request, 'index.html')
        else:
            context = {'msg':'일치하는 회원 정보가 없습니다. 다시 시도해주세요.'}
            return render(request, 'login.html', context)


def logout(request):
    if request.session.get('s_id'):
        request.session.clear()
    
    return redirect('/')


def join01(req):
    return render(req, 'join01_terms.html')


def join02(req):
    return render(req, 'join02_info_input.html')


def idcheck(req):
    id = req.GET.get('user_id', None)  # ajax에서 넘어온 user_id

    try :
        qs = Member.objects.get(m_id=id)
    except :
        qs = None


    if qs is None :   # 중복되는 아이디가 0이면 = 사용가능한 아이디면
        context = {'result':'사용 가능'}
    else :
        context = {'result':'사용 불가'}

    return JsonResponse(context)


def join03(req):
    return render(req, 'join03_success.html')
