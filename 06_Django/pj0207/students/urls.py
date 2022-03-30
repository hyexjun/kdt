from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('reg/', views.regStudent, name='reg'),
    path('regCon/', views.regStuCon, name='regCon'),
    path('regAll/', views.regStuAll, name='regAll'),
    path('<str:name>/<str:major>/regView/', views.regStuView, name='regView'),
    path('<str:name>/regModify/', views.regModify, name='regModify'),
    path('regModiCon/', views.regModiCon, name='regModiCon'),
    path('<str:name>/regDelete/', views.regDelete, name='regDelete'),
]
