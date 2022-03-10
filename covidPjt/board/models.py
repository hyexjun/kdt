from django.db import models
from datetime import datetime


class Fboard(models.Model):
    b_no = models.IntegerField(default=0,primary_key=True)
    b_title = models.CharField(max_length=1000)
    b_content = models.TextField()
    b_date = models.DateTimeField(default=datetime.now(),blank=True)
    b_hit = models.IntegerField(default=1)
    
    def __str__(self):
        return self.b_title


class Comment(models.Model):
    board = models.ForeignKey(Fboard,on_delete=models.CASCADE,null=True)
    c_no = models.IntegerField(default=0,primary_key=True)
    c_pw = models.CharField(max_length=10,blank=True)
    c_content = models.TextField()
    c_date = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    c_spw = models.IntegerField(default='1234')

    def __str__(self):
        return self.c_content