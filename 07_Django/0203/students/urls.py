from . import views    # 모든 것으로부터 오는 것들을 views로..?
from django.urls import path

app_name = 'students'  # 별칭 지정   http://127.0.0.1:8000/students/reg
urlpatterns = [
    path('reg/', views.regStudent, name='reg'),   # 여기 네임은 닉네임..
        # reg/라는 url로 들어오면 views에 있는 regStudent 메소드 가져와
]
