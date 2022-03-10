from datetime import datetime
from django.db import models

# Create your models here.

class Board(models.Model):
    b_no = models.AutoField(primary_key=True)
    b_title = models.CharField(max_length=1000)
    b_content = models.TextField()
    b_date = models.DateTimeField(default=datetime.now(),blank=True)
    b_id = models.CharField(max_length=100)
    b_hit = models.IntegerField(default=1)
    # b_img = models.ImageField(blank=True)
    
    def __str__(self):
        return self.b_title