from django.conf.urls import url
import loginsys.views

urlpatterns = [
    url(r'^signin/', loginsys.views.signin),
    url(r'^signout/', loginsys.views.signout),
    url(r'^$', loginsys.views.register),
]