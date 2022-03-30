from django.db import models

class Member(models.Model):
    m_id = models.CharField(max_length=100, primary_key=True)
    m_pw = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100)
    # m_tel = models.CharField(max_length=20)
    # m_postno = models.CharField(max_length=6, blank=True)
    # m_address = models.CharField(max_length=500, blank=True)
    # m_gender = models.CharField()

    def __str__(self):
        return self.m_name