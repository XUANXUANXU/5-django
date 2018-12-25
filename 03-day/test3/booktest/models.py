from django.db import models


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)  # 图书名称
    bpub_date = models.DateField()  # 发布日期
    bread = models.IntegerField(default=0)  # 阅读量
    bcomment = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄姓名
    hgender = models.BooleanField(default=True)  # 英雄性别
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    hcomment = models.CharField(max_length=200)  # 英雄描述信息
    hbook = models.ForeignKey('BookInfo')


class TypeInfo(models.Model):
    tname = models.CharField(max_length=20)  # 新闻类别


class NewsInfo(models.Model):
    ntitle = models.CharField(max_length=60)  # 新闻标题
    ncontent = models.TextField()  # 新闻内容
    npub_date = models.DateTimeField(auto_now_add=True)  # 新闻发布时间
    ntype = models.ManyToManyField('TypeInfo')
