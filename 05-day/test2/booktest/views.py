from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def login(request):
    return render(request, 'login.html')


def login2(request):
    account = request.POST.get('account')
    pwd = request.POST.get('pwd')
    # print(account,pwd)
    s = ''
    if account == 'xuan' and pwd == '123456':
        s = 'ok'
    else:
        s = 'error'
    # return JsonResponse({'account':account,'pwd':pwd})
    return JsonResponse({'s': s})


def chenggong(request):
    return render(request, 'sueessful.html')
