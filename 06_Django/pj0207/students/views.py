from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student

# Create your views here.
def regStudent(req):
    context = {'uesr_id':'aaa', 'user_pw':'1111'}
    
    return render(req, 'reg.html')

def regStuCon(req):
    name = req.POST.get('name')
    major = req.POST.get('major')
    grade = req.POST.get('grade')
    age = req.POST.get('age')
    gender = req.POST.get('gender')

    qs = Student(s_name=name, s_major=major, s_grade=grade, s_age=age, s_gender=gender)
    qs.save()

    return HttpResponseRedirect(reverse('index'))

def regStuAll(req):
    qs = Student.objects.all()
    s_count = qs.count()
    context = {'stuList':qs, 's_count':s_count}

    return render(req, 'stuList.html', context)

# def regStuView(req):
def regStuView(req, name, major):
    # 위 파라미터 3개, 아래 함수에서 2개지만 위에 3개인 이유는 url에서 이름, 전공을 인자로 받아서다..
    qs = Student.objects.get(s_name=name)
    context = {'stuView':qs}

    return render(req, 'regView.html', context)


def regModify(req, name):
    qs = Student.objects.get(s_name=name)
    context = {'stu':qs}
    return render(req, 'regModify.html', context)


def regModiCon(req):
    name = req.POST.get('name')
    major = req.POST.get('major')
    grade = req.POST.get('grade')
    age = req.POST.get('age')
    gender = req.POST.get('gender')

    qs = Student.objects.get(s_name=name)
    qs.s_major=major
    qs.s_grade=grade
    qs.s_age=age
    qs.s_gender=gender
    qs.save()

    return HttpResponseRedirect(reverse('students:regAll'))


def regDelete(req, name):
    qs = Student.objects.get(s_name=name)
    qs.delete()

    return HttpResponseRedirect(reverse('students:regAll'))