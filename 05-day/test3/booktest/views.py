from django.shortcuts import render
from django.http import JsonResponse
from .models import AccountInfo
# Create your views here.
def login(request):
    return render(request,'login.html')

def login_chuli(request):
    account = request.POST.get('account', '账号error')
    pwd = request.POST.get('pwd', '密码rror')
    l = AccountInfo.objects.filter(account=account)
    if l[0].pwd == pwd:
        return JsonResponse({'status':200})
    else:
        return JsonResponse({'status':407})

def zhuce_chuli(request):
    account = request.POST.get('account', '账号error')
    pwd = request.POST.get('pwd', '密码rror')
    send = {
        'status':200,
        'message':'ok',
        'account':account,
        'pwd': pwd
    }
    if AccountInfo.objects.filter(account=account):
        return JsonResponse({'status':402,'message':'用户已存在'})
    else:
        a = AccountInfo()
        a.account = account
        a.pwd = pwd
        a.save()
        return JsonResponse(send)