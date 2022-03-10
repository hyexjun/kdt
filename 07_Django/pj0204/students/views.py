from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from students.models import Student

# 학생 등록 페이지(reg.html)로 render하는 함수
def regStudent(request):
    return render(request, 'reg.html')

# 학생 등록 페이지에서 입력정보 저장하는 함수
def regStuCon(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    age = request.POST.get('age')
    grade = request.POST.get('grade')
    gender = request.POST.get('gender')
    
    qs = Student(s_name=name, s_major=major, s_age=age, s_grade=grade, s_gender=gender)
    qs.save()

    return HttpResponseRedirect(reverse('index'))


    

# 전체 학생 리스트
def regStuAll(request):
    qs = Student.objects.all()
    context = {'stuList':qs}
    
    return render(request, 'stuList.html', context)
    # 넘길 html 페이지가 있을 때 render 씀