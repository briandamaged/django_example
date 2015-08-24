
from itertools import groupby

from django.shortcuts import render

from aqa.models          import Assessment
from aqa.decorators.auth import login_required

class _AssessmentsByArticle(object):
  def __init__(self, article, assessments):
    self.article     = article
    self.assessments = assessments

  def anchor(self):
    return "assessments_%i" % (self.article.id ,)

  def __str__(self):
    if self.article:
      return str(self.article.title)
    else:
      return "<UNDEFINED ARTICLE>"


def _group_assessments_by_article(assessments):
  for article, items in groupby(assessments, lambda a: a.article):
    yield _AssessmentsByArticle(
      article     = article,
      assessments = list(items)
    )




@login_required
def show_me(req):
  user        = req.user
  assessments = user.assessments \
                    .prefetch_related("article") \
                    .order_by("article") \
                    .all()

  assessment_groups = list(_group_assessments_by_article(assessments))

  # We're passing in the user explicitly so that we
  # have the option to reuse the same templates for
  # the administrative views.
  return render(req, 'aqa/users/show.html', {
    "user":              user,
    "assessment_groups": assessment_groups
  })


@login_required
def show_my_assessment(req, assessment_id):
  user       = req.user
  assessment = user.assessments \
                  .filter(id = assessment_id) \
                  .prefetch_related("answers__question", "article") \
                  .get()



  return render(req, 'aqa/users/show_assessment.html', {
    "user":       user,
    "assessment": assessment,
    "answers":    assessment.answers.all()
  })

