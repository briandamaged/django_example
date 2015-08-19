from django.contrib import admin
from .models import Assessment, Question, UserAnswer


class QuestionInline(admin.StackedInline):
  model = Question
  extra = 0


class AssessmentAdmin(admin.ModelAdmin):
  inlines = [QuestionInline]

admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Question)
admin.site.register(UserAnswer)

