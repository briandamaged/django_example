from django.shortcuts import render

from . import articles


def index(req):
  return render(req, "aqa/welcome.html", {
    "things": [
      "One", "Two", "Three"
    ]
  })
