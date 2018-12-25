from django.shortcuts import render, redirect, reverse
from .models import Banner, Post, FriendlyLink, BlogCategory, Comment, Tags
from userapp.models import BlogUser
from django.views.generic.base import View
from django.db.models import Q

from pure_pagination import Paginator, PageNotAnInteger


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
