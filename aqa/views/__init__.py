from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
  return render(req, "aqa/welcome.html", {
    "things": [
      "One", "Two", "Three"
    ]
  })
