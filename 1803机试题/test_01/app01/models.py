from django.db import models

# Create your models here.

class Contact_zxx(models.Model):
    name_zxx = models.CharField('名字',max_length=30)
    email_zxx = models.EmailField('邮箱',max_length=30)
    phone_zxx = models.CharField('手机',max_length=30)
    comments_zxx = models.TextField('评论')

    def __str__(self):
        return self.name_zxx


    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
