from django.shortcuts import render

from aqa.models import Article

def index(req):
  articles = Article.objects.all()

  return render(req, 'aqa/articles/index.html', {
    "articles": articles
  })


def show(req, article_id):
  article = Article.objects.get(id = article_id)

  return render(req, 'aqa/articles/show.html', {
    "article": article
  })

