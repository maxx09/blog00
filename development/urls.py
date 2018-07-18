from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/$', views.list_page, name='list'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
]