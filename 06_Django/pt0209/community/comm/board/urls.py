from . import views
from django.urls import include, path

app_name='board'
urlpatterns = [
    path('customer/notice/', views.notice,name='notice'),      # 공지사항 리스트
    path('<str:b_no>/event/event_view/', views.event_view,name='event_view'),  # 이벤트뷰
    
    
    path('event/comlist/', views.comlist,name='comlist'),      # 댓글 리스트
    path('event/commwrite/', views.commwrite,name='commwrite'), # 댓글 저장
    path('event/commdelete/', views.commdelete,name='commdelete'), # 댓글 삭제
    path('event/commupdateok/', views.commupdateok,name='commupdateok'), # 댓글 수정저장
    
    
    path('blist/', views.blist,name='blist'),                  # 게시판리스트
    path('bwrite/', views.bwrite,name='bwrite'),               # 글쓰기form
    path('bwriteOk/', views.bwriteOk,name='bwriteOk'),         # 글쓰기저장
    path('<str:b_no>/bview/', views.bview,name='bview'),       # 뷰페이지
    path('<str:b_no>/bmodify/', views.bmodify,name='bmodify'), # 수정form
    path('bmodifyOk/', views.bmodifyOk,name='bmodifyOk'),      # 수정저장
    path('<str:b_no>/bdelete/', views.bdelete,name='bdelete'), # 삭제
    path('<str:b_no>/breply/', views.breply,name='breply'),    # 답글쓰기form
    path('breplyOk/', views.breplyOk,name='breplyOk'),         # 답글쓰기저장
    # 공공데이터
    path('publicData/', views.publicData,name='publicData'),   # 공공데이터
    path('publicData2/', views.publicData2,name='publicData2'),   # 공공데이터
]
