from django.db    import models as m
from django.utils import timezone

# Create your models here.

class Assessment(m.Model):
  author       = m.ForeignKey('auth.User')

  title        = m.CharField(max_length = 128)
  description  = m.TextField()

  created_at   = m.DateTimeField(default = timezone.now)
  published_at = m.DateTimeField(blank = True, null = True)


  def is_published(self):
    return self.is_published is not None

  def publish(self):
    self.published_at = timezone.now()
    self.save()


  def unpublish(self):
    self.published_at = None
    self.save()

  def __str__(self):
    # It's unsafe to assume that self.title will always be
    # a basestring.  So, invoke str(...) to be safe.
    return str(self.title)

