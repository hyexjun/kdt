from . import views
from django.urls import include, path

app_name=''
urlpatterns = [
    path('', views.index,name='index'),
]
