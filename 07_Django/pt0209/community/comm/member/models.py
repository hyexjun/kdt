from django.db import models

# Create your models here.
class Member(models.Model):
    m_id = models.CharField(max_length=30,primary_key=True)
    m_pw = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.m_name
