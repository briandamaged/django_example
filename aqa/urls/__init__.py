
from django.conf.urls import url, include

from . import articles

from aqa import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/', include(articles))
]
