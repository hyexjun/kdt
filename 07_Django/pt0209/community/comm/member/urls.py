from . import views
from django.urls import include, path

app_name='member'
urlpatterns = [
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('join01/', views.join01,name='join01'),
    path('join02/', views.join02,name='join02'),
    path('idcheck/', views.idcheck,name='idcheck'),  #중복확인페이지
]
