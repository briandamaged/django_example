"""
TODO:
  1.  The following constraints are not being honored when
      running the code through `python manage.py shell`:

        * blank = false
        * null  = false

      I suspect that this is because I'm using sqlite3 as the
      database backend during development.

"""

from django.db    import models as m, transaction
from django.utils import timezone

# This model seems like it's generally useful.  So, I'm
# pulling it into this module for convenience.
from django.contrib.auth.models import User


# Ensures that text does not exceed the specified length
from aqa.lib import truncate


class Article(m.Model):
  """
  Represents an article w/ instructional content of some kind.
  The article's author can also specify one or more Questions
  to check the reader's comprehension.

  TODO:

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

  passing_score = m.IntegerField(default = 1)

  created_at   = m.DateTimeField(default = timezone.now)
  published_at = m.DateTimeField(blank = True, null = True)


  @property
  def trimmed_title(self):
    return truncate(self.title, 25)

  @property
  def trimmed_content(self):
    return truncate(self.content, 100)

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


  def create_assessment(self, user, answers):
    """
    Generates a new Assessment instance.  Due to the way that
    Django handles one-to-many relationships, this method also
    needs to immediately persist the data in the db.
    """

    with transaction.atomic():
      a = Assessment(
        article = self,
        user    = user,
        score   = 0
      )
      a.save()


      for q in self.questions.all():
        aa = AssessmentAnswer(
          question = q,
          value    = answers.has_key(q.id)
        )

        # Count up the correct answers
        if aa.is_correct:
          a.score = a.score + 1

        a.answers.add(aa)



      a.save()

    return a


  def create_quiz_form(self):
    """
    Dynamically generates a Form class that is tailored
    to this specific Article instance.

    See, Python?  Meta-programming isn't so bad! :-P
    """
    from django import forms as f

    class MyForm(f.Form):

      def answer_data(self):
        """
        Grabs ONLY the answer data that applies to this form.
        This prevents end-users from adding answers to Questions
        that were not part of this form.
        """
        retval = {}
        for name in self.fields:
          if self.data.has_key(name):
            # Remove the "q_" prefix for easier processing
            key         = int(name.replace("q_", ""))
            retval[key] = self.data[name]


        return retval

      for q in self.questions.all():
        field_name = "q_" + str(q.id)

        vars()[field_name] = f.BooleanField(
          label = q.prompt,
          required = False
        )

    return MyForm


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
  article = m.ForeignKey(Article, related_name = "questions")

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
  user    = m.ForeignKey('auth.User', related_name = "assessments")
  article = m.ForeignKey(Article)

  created_at = m.DateTimeField(default = timezone.now)

  score   = m.IntegerField(default = 0)





class AssessmentAnswer(m.Model):
  """
  Represents the way that a User answered a Question during
  an Assessment.
  """
  assessment = m.ForeignKey(Assessment, related_name = "answers")
  question   = m.ForeignKey(Question, related_name = "answers")

  value      = m.BooleanField(
    "They answered...",   # Used by admin interface
    choices = (
      (True, "Yes"),
      (False, "No")
    ),
    default = True
  )


  @property
  def is_correct(self):
    return self.question.correct_answer == self.value

  @property
  def is_incorrect(self):
    return self.question.correct_answer != self.value

  def __str__(self):
    return str(self.value)

