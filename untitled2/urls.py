"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from resume import views

app_name = "resume"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'resume/(?P<pk>[0-9]+)/$', views.detail, name="detail"),
    url(r'resume2/(?P<pk>[0-9]+)/$', views.detail2, name="detail2"),
    url(r'resume3/(?P<pk>[0-9]+)/$', views.detail3, name="detail3"),
    url(r'resume4/(?P<pk>[0-9]+)/$', views.detail4, name="detail4"),
    url(r'^search/$',views.search,name='search'),
]
