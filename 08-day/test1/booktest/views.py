from django.shortcuts import render,redirect
from .models import PicTest
from django.conf import settings
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.
def show(request):
    p = PicTest.objects.all()
    ctx={
        'p':p
    }
    return render(request,'show.html',ctx)

def upload_show(request):
    return render(request,'upload_images.html')

def upload_handle(request):
    f1 = request.FILES.get('pic')
    fname = '{}/booktest/{}'.format(settings.MEDIA_ROOT,f1.name)
    with open(fname,'wb') as pic:
        for c in f1.chunks():
            pic.write(c)

        p = PicTest()
        p.pic_url = 'booktest/{}'.format(f1.name)
        p.save()
    return redirect(reverse('show'))