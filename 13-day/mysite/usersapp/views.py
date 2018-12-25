from django.shortcuts import render
from .models import User
# Create your views here.
from django.shortcuts import redirect
from .forms import UserForm,RegisterForm


# Create your views here.


def index(request):
    pass
    return render(request, 'index.html')


def login(request):
    # 不允许重复登录
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写内容'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    # 通过下面三句话　往session字典里面写入用户状态和数据
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = '密码不正确'
            except:
                message = '用户不存在'
        return render(request,'login.html',locals())
    login_form = UserForm()
    return  render(request,'login.html',locals())


def register(request):



    register_form = RegisterForm()
    return render(request, 'register.html',locals())


def logout(request):
    """退出登录后重定向到首页"""
    if not request.session.get('is_login',None):
        # 如果本来就未登录,也就没有登出一说
        return redirect('/index/')
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']

    return redirect("/index/")
