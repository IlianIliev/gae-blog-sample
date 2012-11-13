from django.conf.urls import *

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^articles/$', views.list_articles, name='list-articles'),
    url(r'^articles/add/$', views.add_edit, name='add-article'),
    url(r'^articles/edit/(?P<key>.+)/$', views.add_edit, name='edit-article'),
    url(r'^articles/delete/(?P<key>.+)/$', views.delete_article, name='delete-article'),
    url(r'(?P<slug>.+)/$', views.single_article, name='single-article'),
)