import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Album(models.Model):
    artist = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('polls:index')

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text