from datetime import datetime
from django.db import models

# Create your models here.
class Freeboard(models.Model):
    b_no = models.AutoField(primary_key=True)
    b_id = models.CharField(max_length=100) # 원래는 외래키여야 하는데 지금은 없으니까 걍 캐릭터필드로 ㄱㄱ
    b_title = models.CharField(max_length=1000)
    b_content = models.TextField()
    b_date = models.DateTimeField(default=datetime.now(), blank=True)
    b_hit = models.IntegerField(default=1)
    # b_img = models.ImageField(blank=True) # 파일 첨부할 때 쓰는 거

    def __str__(self):
        return self.b_title
    