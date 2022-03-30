from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('board/', include('board.urls')),
    path('member/', include('member.urls')),
    path('blockhtml/', include('blockhtml.urls')),
]


# 파일 업로드 시 url 구성
# 위 url 끝나는 대괄호 ] 옆에 + [ 내용 적기 ] 해도 됨
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# /media 라고 url 달고 들어오는 애들은 실제 media 폴더