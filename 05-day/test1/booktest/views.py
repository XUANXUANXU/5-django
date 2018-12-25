from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def join1(request):
    return render(request, 'join.html')


def join2(request):
    return JsonResponse({'a': 'hello', 'b': 'world'})


def join3(request):
    z = request.POST.get('a')
    x = request.POST.get('b')
    return JsonResponse({'l':z,'ll':x})