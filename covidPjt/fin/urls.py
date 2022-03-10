from . import views
from django.urls import include, path


app_name = 'fin'
urlpatterns = [
    path('chart/', views.chart, name= 'chart' ),
    path('fview/', views.fview, name= 'fview' ),
    path('code_DailyCovid/', views.code_DailyCovid, name= 'code_DailyCovid' ),
    path('code_totalCovid/', views.code_totalCovid, name= 'code_totalCovid' ),
    path('code_totalVaccine/', views.code_totalVaccine, name= 'code_totalVaccine' ),
    path('code_dailyVaccine/', views.code_dailyVaccine, name= 'code_dailyVaccine' ),
    path('DailyCovid/', views.DailyCovid, name= 'DailyCovid' ),
    path('TotalCovid/', views.TotalCovid, name= 'TotalCovid' ),
    path('DailyVaccine/', views.DailyVaccine, name= 'DailyVaccine' ),
    path('TotalVaccine/', views.TotalVaccine, name= 'TotalVaccine' ),
    path('codeDate/', views.codeDate, name= 'codeDate' ),
    path('covidspread/', views.covidspread, name= 'covidspread' ),
]