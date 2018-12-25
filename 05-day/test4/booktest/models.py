from django.db import models

# Create your models here.
class AccountInfo(models.Model):
    account = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)