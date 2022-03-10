from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.core.paginator import Paginator
from board.models import Fboard
from django.db.models import Max,Min,Avg 

def blist(request):
    qs = Fboard.objects.all().order_by('-b_no')
    paginator=Paginator(qs,15)
    nowpage=int(request.GET.get('nowpage',1))
    blist=paginator.get_page(nowpage)
    context = {'blist':blist,'nowpage':nowpage}
    return render(request,'blist.html', context)

def bview(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    qs.b_hit += 1
    qs.save()
    context={'board':qs}
    return render(request,'bview.html',context)

def bwrite(request):
    return render(request, 'bwrite.html')

def bwriteOk(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    no = Fboard.objects.aggregate(max_b_no=Max('b_no'))
    max_no = no['max_b_no'] 
    max_no += 1         
    b_no = max_no
    qs = Fboard(b_no=b_no,b_title=title,b_content=content)
    qs.save()
    return redirect('board:blist')

def bmodify(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    context={'board':qs}
    return render(request,'bmodify.html',context)

def bmodifyOk(request):
    b_no = request.POST.get('b_no')
    b_title = request.POST.get('b_title')
    b_content = request.POST.get('b_content')
    qs = Fboard.objects.get(b_no=b_no)
    qs.b_title = b_title
    qs.b_content = b_content
    qs.save()
    return render(request,'bview.html',{"board":qs})

def bdelete(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    qs.delete()
    return redirect('board:blist')
    
    
