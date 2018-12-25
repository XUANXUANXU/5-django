from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class BlogUser(AbstractUser):
    nikename = models.CharField('昵称',max_length=20,default='')

class EmailVerifyRecord(models.Model):
    code = models.CharField('验证码',max_length=50,default='')
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField('验证码类型',choices=(('register','注册'),('forget','找回密码'),('update_email','修改邮箱')),max_length=30)
    send_time = models.DateTimeField('发送时间',auto_now_add=True)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}--{}'.format(self.code, self.email)