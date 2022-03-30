from datetime import datetime
from django.db import models
from member.models import Member

# Create your models here.

class Board(models.Model):
    # b_no = models.AutoField(primary_key=True)
    b_no = models.IntegerField(default=0, primary_key=True)
    b_title = models.CharField(max_length=1000)
    b_content = models.TextField()
    b_date = models.DateTimeField(default=datetime.now(),blank=True)
    # b_id = models.CharField(max_length=100)
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING, null=True)

    b_group = models.IntegerField(default=0)
    b_step = models.IntegerField(default=0)
    b_indent = models.IntegerField(default=0)

    b_hit = models.IntegerField(default=1)
    b_img = models.ImageField(blank=True)
    
    def __str__(self):
        return self.b_title



class Comment(models.Model):
    c_no = models.IntegerField(default=0, primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    c_pw = models.CharField(max_length=10, blank=True)
    c_content = models.TextField()
    c_date = models.DateTimeField(default=datetime.now(), blank=True)
    
    def __str__(self):
        return self.c_content