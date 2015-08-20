
from django.conf.urls import url

from aqa import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^articles$', views.articles.index, name="all_articles"),
    url(r'^articles/(?P<article_id>\d+)$', views.articles.show, name="show_article")
]
