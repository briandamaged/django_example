from django.shortcuts import render, redirect

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


def quiz(req, article_id):
  article = Article.objects \
                   .prefetch_related("questions") \
                   .get(id = article_id)

  TheForm = article.create_quiz_form()


  if req.method == "POST":
    form = TheForm(req.POST)

    # Note: This will basically ALWAYS be true because the
    #       form consists entirely of non-required BooleanFields.
    #       I can think of ways to address this, but they would
    #       involve fighting Django.
    if form.is_valid():
      from django.http import JsonResponse

      answers = form.answer_data()

      a = article.create_assessment(
        user    = req.user,
        answers = answers
      )

      return redirect("show_me")

  else:  # GET, or any other method
    form = TheForm()


  return render(req, 'aqa/articles/quiz.html', {
    "article": article,
    "form":    form
  })

