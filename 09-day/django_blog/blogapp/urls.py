from django.conf.urls import url,include
from blogapp import views
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^blog_list/(?P<tid>\d+)/$',views.blog_list,name='blog_list'),
    url(r'^show/(\d+)/$',views.show,name='show'),
    url(r'^comment_handle/$',views.comment_handle,name='comment_handle')
]