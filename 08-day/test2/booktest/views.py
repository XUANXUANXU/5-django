from django.shortcuts import render
from django.core.paginator import Paginator,Page
from .models import Areas
# Create your views here.
def show(request,pIndex):
    list = Areas.objects.filter(aParent_id__isnull=True)
    p = Paginator(list,10)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    ctx = {
        'list':list2,
        'plist':plist,
        'pIndex':pIndex
    }
    return render(request,'show.html',ctx)