from django.contrib import admin
from .models import Article, Question, AssessmentAnswer


class QuestionInline(admin.StackedInline):
  model = Question
  extra = 0


class ArticleAdmin(admin.ModelAdmin):
  inlines = [QuestionInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Question)
admin.site.register(AssessmentAnswer)

