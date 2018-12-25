from django.conf.urls import url
from booktest import views
urlpatterns = [
    url(r'^join1/$',views.join1),
    url(r'^join2/$',views.join2),
    url(r'^join3/$',views.join3)
]