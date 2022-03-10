from django.db import models

# Create your models here.


from django.db import models
from django.forms import CharField


# Create your models here.

class dailycovid(models.Model):
    strdate= models.CharField(max_length=30, primary_key=True)
    intdate= models.IntegerField(default=0)
    deathCnt = models.IntegerField( default=0)
    decideCnt= models.IntegerField( default=0)

    def __str__(self):
        return self.strdate
    
class dailyvaccine(models.Model):
    strdate= models.CharField(max_length=30, primary_key=True) # str 형식의 date
    intdate= models.IntegerField(default=0) # int 형식의 date
    firstCnt= models.IntegerField(default=0) # 해당 날짜 1차 접종자 수
    secondCnt = models.IntegerField( default=0) # 해당 날짜 2차 접종자 수
    thirdCnt= models.IntegerField( default=0) # 해당 날짜 3차 접종자 수
    totalFirstCnt= models.IntegerField( default=0) # 누적 1차 접종자 수
    totalSecondCnt= models.IntegerField( default=0) # 누적 2차 접종자 수
    totalThirdCnt= models.IntegerField( default=0) # 누적 3차 접종자 수

    def __str__(self):
        return self.strdate
