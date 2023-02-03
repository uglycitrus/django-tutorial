import datetime

from django.db import models
from django.utils import timezone

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_question_id = self.question_id

    def __str__(self):
        return self.choice_text


class Tag(models.Model):

    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    tag_text = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_text
