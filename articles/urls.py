from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from  .import views #since views present in the same directory

app_name='articles'  #namespace

urlpatterns = [
    url(r'^$',views.article_list,name='list'),
    url(r'^create/$',views.article_create,name='create'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail,name='detail'),

]
 