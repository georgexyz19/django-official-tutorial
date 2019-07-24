# polls/models.py

from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        one_day_later = self.pub_date >= now - datetime.timedelta(days=1)
        not_in_future = now >= self.pub_date
        return one_day_later and not_in_future
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True # for symbol X
    was_published_recently.short_description = 'Published Recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

