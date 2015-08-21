
from django.conf.urls import url, include

from . import articles, session

from aqa import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/', include(articles)),
    url(r'^session/', include(session))
]
