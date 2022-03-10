from django.urls import path
from . import views

app_name = "students"
urlpatterns = [
    path('reg/', views.regStudent, name='reg'),
    # 추가로 더 만들어야 하는 페이지가
    # 전체학생리스트랑
    path('regCon/', views.regStuCon, name='regCon'),
    path('regAll/', views.regStuAll, name='regAll'),
    path('regSearch/', views.regStuSearch, name='regSearch'),
    path('regSearCon/', views.regStuSearCon, name='regSearCon'),
]
