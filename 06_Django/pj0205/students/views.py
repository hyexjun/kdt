from ast import If
from msilib.schema import RadioButton
from operator import contains
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student


def regStudent(request):
    return render(request, 'reg.html')


def regStuCon(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')

    qs = Student(s_name=name, s_age=age, s_major=major, s_grade=grade, s_gender=gender)
    qs.save()

    return HttpResponseRedirect(reverse('index'))


def regStuAll(request):
    qs = Student.objects.all()
    context = {'stuList': qs}

    return render(request, 'stuList.html', context)


# 단순하게 메인페이지에서 조회 페이지로 이동하는 용
def regStuSearch(request):
    return render(request, 'search.html')


# 실제 조회 페이지에서 검색버튼 눌렀을 때 그 값으로 db에서 조회하는 거
def regStuSearCon(request):
    keyword = request.GET['keyword']
    qs = Student.objects.filter(s_name__contains=keyword)
    # qs = Student.objects.filter(RadioButton__contains=keyword)
    # 라디오에서 선택한 속성값으로 필터되는 거 만들고 싶다..
    context = {'searchList': qs}
    return render(request, 'search.html', context)
