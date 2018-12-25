from django.conf.urls import url
from booktest import views

urlpatterns = [
    #url(r'^index/(\d+)/$',views.index)
    #url(r'^index/(\d+)/([a-z]+)/$',views.index)
    url(r'^index/$',views.index),
    url(r'^index2/$',views.index2)
]