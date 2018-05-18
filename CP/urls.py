"""CP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^', include('loginsys.urls')),
    url(r'^home/', TemplateView.as_view(template_name='index.html')),
    url(r'^all-events/', TemplateView.as_view(template_name='all-events.html')),
    url(r'^prev-events/', TemplateView.as_view(template_name='prev-events.html')),
    url(r'^next-events/', TemplateView.as_view(template_name='next-events.html')),
    url(r'^one-event/', TemplateView.as_view(template_name='one-event.html')),
    url(r'^organize/', TemplateView.as_view(template_name='organize.html')),
    url(r'^donate/', TemplateView.as_view(template_name='donate.html')),
    url(r'^profile/', TemplateView.as_view(template_name='profile.html')),
    url(r'^admin/', admin.site.urls),
]
