from django.shortcuts import render

# main페이지
def index(request):
    return render(request,'index.html')