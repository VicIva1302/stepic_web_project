from django.db import models

# Create your models here.
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new():
        return self.order_by('-added_at')
    def popular():
        return self.order_by('-rating')

@python_2_unicode_compatible
class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(default="", max_length=255)
    text = models.TextField(default="")
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="fk_author")
    likes =  models.ManyToManyField(User, related_name='fk_likes_set',  blank=True)
    def __str__(self):
        return self.title
    def get_url(self):
        return "/question/{}/".format(self.id)

@python_2_unicode_compatible
class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

