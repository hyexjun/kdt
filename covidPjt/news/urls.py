from . import views
from django.urls import path

app_name = 'news'
urlpatterns = [
    path('nlist/', views.nlist, name='nlist'),
    # path('nwrite/', views.nwrite, name='nwrite'),
    # path('nwriteOk/', views.nwriteOk,name='nwriteOk'),
    # path('<str:n_no>/nview/', views.nview,name='nview'),
    # path('<str:n_no>/nmodify/', views.nmodify,name='nmodify'),
    # path('nmodifyOk/', views.nmodifyOk,name='nmodifyOk'),      
    # path('<str:n_no>/ndelete/', views.ndelete,name='ndelete'), 
    
    # path('comlist/', views.comlist,name='comlist'), 
    # path('commwrite/', views.commwrite,name='commwrite'),    
    # path('commupdateok/', views.commupdateok,name='commupdateok'),
    # path('commdelete/', views.commdelete,name='commdelete'),    
 ]
