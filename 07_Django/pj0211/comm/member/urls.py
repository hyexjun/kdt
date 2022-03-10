from . import views
from django.urls import path

app_name = 'member'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
