from . import views
from django.urls import path

app_name = 'member'
urlpatterns = [
    # path('mwrite/', views.mwrite, name='mwrite'),
    path('login/', views.login, name='login'),
    path('loginOk/', views.loginOk, name='loginOk'),
    path('logout/', views.logout, name='logout'),
]
