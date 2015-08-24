
from django.conf.urls import url

import aqa.views.users as v

urlpatterns = [
  url(r'me$', v.show_me, name="show_me"),
  url(r'me/assessments/(?P<assessment_id>\d+)$', v.show_my_assessment, name="show_my_assessment")
]
