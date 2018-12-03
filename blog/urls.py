"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path,include
from django.conf.urls import url,include
from  .import views #since views present in the same directory

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from articles import views as article_views #sicne view already imported

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^articles/',include('articles.urls')),
    url(r'^about/$',views.about),
    url(r'^$',article_views.article_list,name="home"),#root url
    url(r'^accounts/',include('accounts.urls')),
    # path('admin/', admin.site.urls),
    # path('about/',views.about),
    # path('homepage/',views.homepage)
    # url('articles/', include('articles.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)