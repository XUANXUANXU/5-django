from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo, HeroInfo


# Create your views here.
def index(request):
    return HttpResponse('哈哈哈哈哈哈哈')


def index2(request):
    b = BookInfo.objects.all()
    a = {
        'hero': b
    }
    return render(request, 'index2.html', a)
