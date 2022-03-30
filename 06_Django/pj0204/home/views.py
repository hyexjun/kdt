from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'user_id':'AAA', 'nickname':'aaa'}    # count=2day를 변수 count 전송시킴
    return render(request, 'index.html', context)