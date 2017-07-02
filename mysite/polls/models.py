import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

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

class Genres(models.Model):
    GenreOptions = (
        ('ACT', 'action'),
        ('COM', 'comedy'),
    )
    type = models.CharField(max_length=20, choices=GenreOptions)

class Album(models.Model):
    artist = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('polls:index')

GenderOptions = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),
)

class Questions(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=20, choices=GenderOptions)
