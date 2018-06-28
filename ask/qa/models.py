from django.db import models

# Create your models here.
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class QuestionManager(models.Manager):
    def new():
        #pass
        return self.order_by('-id')
    def popular():
        #return self.order_by('-rating')
        pass

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
    def get_absolute_url(self):
        return reverse('question', kwargs={'pk': self.id})

class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def get_url(self):
        return format(self.question.get_url())
