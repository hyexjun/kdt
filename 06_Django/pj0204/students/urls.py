from . import views
from django.urls import include, path

app_name = "students"
urlpatterns = [
    # 이하 주소 reg/로 들어올 때 views의 regStudent함수를 실행시켜줘
    path('reg/', views.regStudent, name='reg'),
    path('regCon/', views.regStuCon, name='regCon'),
    path('regAll/', views.regStuAll, name='regAll'),
]
