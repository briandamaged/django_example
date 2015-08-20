
from django.conf.urls import url

import aqa.views.articles as v

urlpatterns = [
    url(r'^$', v.index, name="all_articles"),
    url(r'^(?P<article_id>\d+)$', v.show, name="show_article")
]
