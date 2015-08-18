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



class Assessment(m.Model):
  author       = m.ForeignKey('auth.User')

  title        = m.CharField(max_length = 128)
  description  = m.TextField()

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
  assessment = m.ForeignKey(Assessment)

  prompt = m.TextField();

  # TODO: Eventually, we would want to extract this into a
  #       polymorphic model so that we could support many
  #       different types of answers.
  correct_answer = m.BooleanField()


  def __str__(self):
    return str(self.prompt)



# This class is called "UserAnswer" because it's the answer
# that was provided by a specific User.  
class UserAnswer(m.Model):
  answerer = m.ForeignKey('auth.User')

  question = m.ForeignKey(Question)
  value    = m.BooleanField()


  def is_correct(self):
    return self.question.correct_answer == self.value

  def is_incorrect(self):
    return self.question.correct_answer != self.value

  def __str__(self):
    return str(self.value)



