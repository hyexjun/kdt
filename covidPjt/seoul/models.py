# Create your models here.
from django.db import models

class Patientadd(models.Model):

    date = models.DateTimeField(
        null=False, default=0, max_length=100, primary_key=True)
    gangnam = models.IntegerField(null=False, default=0)
    gangdong = models.IntegerField(null=False, default=0)
    gangbuk = models.IntegerField(null=False, default=0)
    gangseo = models.IntegerField(null=False, default=0)
    gwanak = models.IntegerField(null=False, default=0)
    gwangjin = models.IntegerField(null=False, default=0)
    guro = models.IntegerField(null=False, default=0)
    geumcheon = models.IntegerField(null=False, default=0)
    nowon = models.IntegerField(null=False, default=0)
    dobong = models.IntegerField(null=False, default=0)
    ddm = models.IntegerField(null=False, default=0)
    dongjak = models.IntegerField(null=False, default=0)
    mapo = models.IntegerField(null=False, default=0)
    sdm = models.IntegerField(null=False, default=0)
    seocho = models.IntegerField(null=False, default=0)
    seongdong = models.IntegerField(null=False, default=0)
    seongbuk = models.IntegerField(null=False, default=0)
    songpa = models.IntegerField(null=False, default=0)
    yangcheon = models.IntegerField(null=False, default=0)
    ydp = models.IntegerField(null=False, default=0)
    yongsan = models.IntegerField(null=False, default=0)
    ep = models.IntegerField(null=False, default=0)
    jongno = models.IntegerField(null=False, default=0)
    junggu = models.IntegerField(null=False, default=0)
    jungnang = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.date


class Patientsum(models.Model):

    date = models.DateTimeField(
        null=False, default=0, max_length=100, primary_key=True)
    gangnam = models.IntegerField(null=False, default=0)
    gangdong = models.IntegerField(null=False, default=0)
    gangbuk = models.IntegerField(null=False, default=0)
    gangseo = models.IntegerField(null=False, default=0)
    gwanak = models.IntegerField(null=False, default=0)
    gwangjin = models.IntegerField(null=False, default=0)
    guro = models.IntegerField(null=False, default=0)
    geumcheon = models.IntegerField(null=False, default=0)
    nowon = models.IntegerField(null=False, default=0)
    dobong = models.IntegerField(null=False, default=0)
    ddm = models.IntegerField(null=False, default=0)
    dongjak = models.IntegerField(null=False, default=0)
    mapo = models.IntegerField(null=False, default=0)
    sdm = models.IntegerField(null=False, default=0)
    seocho = models.IntegerField(null=False, default=0)
    seongdong = models.IntegerField(null=False, default=0)
    seongbuk = models.IntegerField(null=False, default=0)
    songpa = models.IntegerField(null=False, default=0)
    yangcheon = models.IntegerField(null=False, default=0)
    ydp = models.IntegerField(null=False, default=0)
    yongsan = models.IntegerField(null=False, default=0)
    ep = models.IntegerField(null=False, default=0)
    jongno = models.IntegerField(null=False, default=0)
    junggu = models.IntegerField(null=False, default=0)
    jungnang = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.date


class Death(models.Model):
    date = models.DateTimeField(null=False, default=0, max_length=100)
    location = models.CharField(max_length=30)
    deathcnt = models.IntegerField(default=0)
    incdec = models.IntegerField(default=0)
    defCnt = models.IntegerField(default=0)

    def __str__(self):
        return self.location