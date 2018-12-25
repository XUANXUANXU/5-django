from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo,HeroInfo
# Create your views here.


def index(request):
    b = BookInfo.objects.filter(id=1)
    return HttpResponse(b[0].btitle)

