from . import views
from django.urls import path

app_name = ''
urlpatterns = [
    path('', views.index, name='index'),
]
