from django.shortcuts import render
from .models import Contact_zxx
from pure_pagination import Paginator, PageNotAnInteger
# Create your views here.
def index_zxx(request):

    return render(request,'index.html')

def show_zxx(request):



    if request.method == 'POST':
        name = request.POST.get('user')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('msg')


        c = Contact_zxx()
        c.name_zxx = name
        c.email_zxx = email
        c.phone_zxx = phone
        c.comments_zxx = comments
        c.save()

    list = Contact_zxx.objects.all()

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(list, per_page=1, request=request)
    list = p.page(page)
    ctx = {
        'list':list
    }
    return render(request,'show.html',ctx)