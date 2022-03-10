from django.apps import AppConfig


class BlockhtmlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blockhtml'

# 여기 있는 6번줄의 네임 설정이랑
# urls.py에 있는 app_name 설정이랑 뭔 차이임???