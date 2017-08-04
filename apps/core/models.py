from django.db import models


class Sample(models.Model):
    "Sample question model"
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
