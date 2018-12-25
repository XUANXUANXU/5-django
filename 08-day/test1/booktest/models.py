from django.db import models

# Create your models here.
class PicTest(models.Model):
    pic_url = models.ImageField(max_length=300,upload_to='booktest/')