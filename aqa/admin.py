from django.contrib import admin
from .models import Article, Question, Assessment, AssessmentAnswer


class QuestionInline(admin.StackedInline):
  model = Question
  extra = 0

  can_delete = True


class ArticleAdmin(admin.ModelAdmin):
  inlines = [QuestionInline]



class AssessmentAnswerInline(admin.StackedInline):
  model = AssessmentAnswer
  extra = 0

  can_delete = True


class AssessmentAdmin(admin.ModelAdmin):
  inlines = [AssessmentAnswerInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Question)

admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(AssessmentAnswer)

