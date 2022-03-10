from . import views
from django.urls import path

app_name = 'board'
urlpatterns = [
    path('blist/', views.blist, name='blist'),
    path('bwrite/', views.bwrite, name='bwrite'),
    path('bwriteOk/', views.bwriteOk, name='bwriteOk'),
]
