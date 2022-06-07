from datetime import datetime
from django.db import models
from django.forms import DateTimeField

# Create your models here.


class Member(models.Model):
    u_id = models.CharField(max_length=100, primary_key=True)
    u_pw = models.CharField(max_length=100)
    u_name = models.CharField(max_length=100)
    u_date = models.DateTimeField(default=datetime.now(), blank=True)
    u_hobby = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.u_id
