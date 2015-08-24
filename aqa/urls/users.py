
from django.conf.urls import url

import aqa.views.users as v

urlpatterns = [
  url('me$', v.me, name="show_me")
]
