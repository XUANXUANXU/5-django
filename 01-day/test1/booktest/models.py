from django.db import models
from datetime import datetime


# Create your models here.
class BookInfo(models.Model):
    bname = models.CharField(max_length=20)
    bdate = models.CharField(default=datetime.now, max_length=50)


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    isdelete = models.BooleanField(default=False)
    bbook = models.ForeignKey('BookInfo')
