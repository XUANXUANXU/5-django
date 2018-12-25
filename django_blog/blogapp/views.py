from django.shortcuts import render, redirect, reverse
from .models import Banner, Post, FriendlyLink, BlogCategory, Comment, Tags,User
from userapp.models import BlogUser
from django.views.generic.base import View
from django.db.models import Q
from .forms import UserForm,RegisterForm
from pure_pagination import Paginator, PageNotAnInteger
import hashlib

class SearchView(View):
    def post(self, request):
        kw = request.POST.get('keyword')
        post_list = Post.objects.filter(Q(title__icontains=kw) | Q(content__icontains=kw))
        ctx = {
            'post_list': post_list
        }
        return render(request, 'search_list.html', ctx)

    # 列表页


def blog_list(request,tid):
    if tid!='0':
        tag = Tags.objects.get(id=tid)
        post_list = tag.post_set.all().order_by('-pub_date')
    else:
        post_list = Post.objects.all().order_by("-pub_date")
    tags_list = Tags.objects.all()
    new_comment_list = Post.objects.filter(comment__content__isnull=False).order_by('-pub_date')

    new_comment_list2 = []
    for blog in new_comment_list:
        if blog in new_comment_list2:
            pass
        else:
            new_comment_list2.append(blog)

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(post_list, per_page=1, request=request)
    post_list = p.page(page)
    ctx = {
        'post_list': post_list,
        'tags_list': tags_list,
        'new_comment_list': new_comment_list2

    }

    return render(request, 'list.html', ctx)


def index(request):
    banner_list = Banner.objects.all()
    recommend_list = Post.objects.filter(recommend=True)
    post_list = Post.objects.order_by('-pub_date').all()
    friend_list = FriendlyLink.objects.all()
    blogcategory_list = BlogCategory.objects.all()
    new_comment_list = Post.objects.filter(comment__content__isnull=False).order_by('-pub_date')
    new_comment_list2 = []

    count = post_list.count()
    for blog in new_comment_list:
        if blog in new_comment_list2:
            pass
        else:
            new_comment_list2.append(blog)
    ctx = {
        'banner_list': banner_list,
        'recommend_list': recommend_list,
        'post_list': post_list,
        'friend_list': friend_list,
        'blogcategory_list': blogcategory_list,
        'new_comment_list': new_comment_list2,
        'count': count

    }
    return render(request, 'index.html', ctx)


def show(request, page):
    page = int(page)
    blog = Post.objects.get(id=page)

    blog.views += 1
    blog.save()

    recomment_list = Post.objects.filter(Q(title__contains=blog.title) | Q(content__contains=blog.title))
    new_comment_list = Post.objects.filter(comment__content__isnull=False).order_by('-pub_date')
    new_comment_list2 = []
    for blogs in new_comment_list:
        if blogs in new_comment_list2:
            pass
        else:
            new_comment_list2.append(blogs)
    ctx = {
        'blog': blog,
        'recomment_list': recomment_list,
        'new_comment_list': new_comment_list2
    }
    return render(request, 'show.html', ctx)


def comment_handle(request):
    blog_id = request.POST.get('blog_id')
    username = request.POST.get('username')
    email = request.POST.get('email')
    comment = request.POST.get('comment-text')
    c = Comment()
    c.user = BlogUser.objects.get(id=1)
    c.content = comment
    c.post = Post.objects.get(id=blog_id)
    c.save()

    return redirect(reverse('blogapp:show', args=(blog_id,)))


def login(request):
    if request.session.get('is_login', None):
        return redirect('/blogapp/index/')

    if request.method == 'POST':
        login_forms = UserForm(request.POST)
        message = ''
        # username = request.POST.get('username',None)
        # password = request.POST.get('password',None)

        if login_forms.is_valid():
            username = login_forms.cleaned_data['username']
            password = login_forms.cleaned_data['password']
            # username = username.strip()
            try:
                user = User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('blogapp:index')
                else:
                    message = '密码错误'
            except:
                message = '该用户不存在'

        return render(request, 'login.html', locals())
    login_forms = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/blogapp/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/blogapp/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/blogapp/index/')
    request.session.flush()
    return redirect('/blogapp/index/')


def hash_code(s,salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()
