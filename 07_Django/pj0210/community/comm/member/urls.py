from django.urls import include, path
from . import views

app_name="member"
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('join01/', views.join01, name="join01"),
    path('join02/', views.join02, name="join02"),
    path('join03/', views.join03, name="join03"),
    path('idcheck/', views.idcheck, name="idcheck"),
]
