from django.shortcuts import render
from django.http import JsonResponse
from .models import AccountInfo


# Create your views here.
def login(request):
    return render(request, 'login.html')


def login_successful(request):
    return render(request, 'login_successful.html')


def register_successful(request):
    return render(request, 'register_successful.html')


def login_handle(request):
    a = request.POST.get('account')
    b = request.POST.get('pwd')
    l = AccountInfo.objects.filter(account=a)
    if l[0].pwd == b:
        return JsonResponse({'status': 200, 'message': '登陆成功'})
    else:
        return JsonResponse({'status': 403, 'message': '登录失败'})


def register_handle(request):
    a = request.POST.get('account')
    b = request.POST.get('pwd')
    if AccountInfo.objects.filter(account=a):
        return JsonResponse({'status': 403, 'message': '用户已存在'})
    else:
        x = AccountInfo()
        x.account = a
        x.pwd = b
        x.save()
        return JsonResponse({'status': 200, 'key': a, 'key2': b})
