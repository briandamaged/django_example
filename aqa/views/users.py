
from django.shortcuts import render

from aqa.models import Assessment

def me(req):
  user        = req.user
  assessments = user.assessments.all()

  # We're passing in the user explicitly so that we
  # have the option to reuse the same templates for
  # the administrative views.
  return render(req, 'aqa/users/show.html', {
    "user":        user,
    "assessments": assessments
  })

