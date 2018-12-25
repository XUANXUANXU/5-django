from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # c = {
    #     'a':accound,
    #     'b':pwd
    # }
    #return HttpResponse('hello world')

    return render(request,'show.html')

# def index2(request):
#     return HttpResponse(request.method)

def index2(request):
    # s = request.GET.get("account")
    # d = request.GET.get("pwd")
    # b="z:{},p:{}".format(s,d)
    s= request.POST.getlist('hobby')
    return HttpResponse(s)



