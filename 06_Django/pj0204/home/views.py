from django.shortcuts import render
# Create your views here.

def index(request):
    # count=2day를 변수 count 전송시킴
    context = {'user_id': 'AAA', 'nickname': 'aaa'}
    return render(request, 'index.html', context)
