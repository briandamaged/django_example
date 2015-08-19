"""
TODO:
  1.  The following constraints are not being honored when
      running the code through `python manage.py shell`:

        * blank = false
        * null  = false

      I suspect that this is because I'm using sqlite3 as the
      database backend during development.

"""

from django.db    import models as m
from django.utils import timezone

# This model seems like it's generally useful.  So, I'm
# pulling it into this module for convenience.
from django.contrib.auth.models import User


class Article(m.Model):
  """
  Represents an article w/ instructional content of some kind.
  The article's author can also specify one or more Questions
  to check the reader's comprehension.

  TODO:

    * Add a passing_grade field.  End-users must achieve this 
      grade before they have "passed" an Assessment.

    * Add a content_format field that will control how the
      content is rendered.  For example: text, markdown, etc.

    * Ideally, we want to prevent authors from modifying an
      Article after it has been published.  Instead, they should
      create a new version of the Article.  But, that workflow
      can be implemented later.
  """
  author       = m.ForeignKey('auth.User')

  title        = m.CharField(max_length = 128)
  content      = m.TextField()

  created_at   = m.DateTimeField(default = timezone.now)
  published_at = m.DateTimeField(blank = True, null = True)


  def is_published(self):
    return self.published_at is not None


  def publish(self):
    self.published_at = timezone.now()
    self.save()
    return self

  def unpublish(self):
    self.published_at = None
    self.save()
    return self

  def __str__(self):
    return str(self.title)



class Question(m.Model):
  """
  Represents a Question about an Article.

  TODO:
    * Add a 'points' field, which indicates the number of points
      that the question is worth.

    * Consider making this class polymorphic so that other types
      of questions can be supported in the future.
  """
  article = m.ForeignKey(Article)

  prompt = m.TextField();

  correct_answer = m.BooleanField(
    "The answer is...",
    choices = (
      (True, "Yes"),
      (False, "No")
    ),
    default = True
  )


  def __str__(self):
    return str(self.prompt)




class Assessment(m.Model):
  """
  After a User reads an Article, they can take an Assessment to
  check their comprehension of the material.
  """
  user    = m.ForeignKey('auth.User')
  article = m.ForeignKey(Article)




class AssessmentAnswer(m.Model):
  """
  Represents the way that a User answered a Question during
  an Assessment.
  """
  assessment = m.ForeignKey(Assessment)

  question   = m.ForeignKey(Question)
  value      = m.BooleanField(
    "They answered...",   # Used by admin interface
    choices = (
      (True, "Yes"),
      (False, "No")
    ),
    default = True
  )


  def is_correct(self):
    return self.question.correct_answer == self.value

  def is_incorrect(self):
    return self.question.correct_answer != self.value

  def __str__(self):
    return str(self.value)

