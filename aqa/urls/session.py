
from django.conf.urls import url

import django.contrib.auth.views as v

login_params = {
  "template_name": "aqa/session/sign_in.html"
}

logout_params = {
  "template_name": "aqa/session/sign_out.html"
}

urlpatterns = [
    url(r'^sign_in$',  v.login,  login_params,  name="sign_in"),
    url(r'^sign_out$', v.logout, logout_params, name="sign_out")
]
