from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from random import Random

def make_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str



def send(request):

    msg = '<a href="http://127.0.0.1:8000/yanzheng/{}/" target="_blank">点击激活</a>'.format(make_random_str(10))
    send_mail('注册激活', '', settings.EMAIL_FROM,
          ['302738630@qq.com'],
          html_message=msg)
    return HttpResponse('ok')

def yanzheng(request,a):
    print(a)
    return HttpResponse('验证成功')


















































