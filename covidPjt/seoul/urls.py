from django.urls import path
from . import views

app_name = 'seoul'
urlpatterns = [
    path('sview/', views.sview, name='sview'),
    path('chartshow/', views.chartshow, name='chartshow'),
]