import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from board.models import Freeboard

# Create your views here.
def blist(req):
    qs = Freeboard.objects.all().order_by('-b_no')
    context = {'blist':qs}
    return render(req, 'blist.html', context)

def bwrite(req):
    return render(req, 'write_view.html')

def bwriteOk(req):
    name = req.POST.get('id')
    title = req.POST.get('title')
    content = req.POST.get('content')
    qs = Freeboard(b_id=name, b_title=title, b_content=content)
    qs.save()

    return HttpResponseRedirect(reverse('board:blist'))

# 게시판 컨텐츠 뷰html으로 넣어줄 예정
def bview(req, b_no):
    qs = Freeboard.objects.get(b_no=b_no)
    qs.b_hit += 1
    context = {'board':qs}
    return render(req, 'content_view.html', context)

def bmodify(req, b_no):
    qs = Freeboard.objects.get(b_no=b_no)
    context = {'board':qs}
    return render(req, 'modify_view.html', context)


def bmodifyOk(req):
    b_no = req.POST.get('no')
    title = req.POST.get('title')
    content = req.POST.get('content')
    qs = Freeboard.objects.get(b_no=b_no)
    qs.b_title = title
    qs.b_content = content
    # qs.b_date = timezone.now()
    qs.save()

    return HttpResponseRedirect(reverse('board:blist'))


def bdelete(req, b_no):
    qs = Freeboard.objects.get(b_no=b_no)
    qs.delete()
    return HttpResponseRedirect(reverse('board:blist'))