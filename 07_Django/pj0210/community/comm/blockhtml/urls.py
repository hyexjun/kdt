from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="blockhtml"
urlpatterns = [
    path('main/', views.main, name='main'),
    path('notice_list/', views.notice_list, name='notice_list'),
    path('notice_read/', views.notice_read, name='notice_read')
]
