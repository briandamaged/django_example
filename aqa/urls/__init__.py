
from django.conf.urls import url, include

from . import articles, session, users

from aqa import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/', include(articles)),
    url(r'^users/', include(users)),
    url(r'^session/', include(session))
]
