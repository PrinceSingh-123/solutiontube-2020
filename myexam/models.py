from __future__ import unicode_literals
from django.db import models

# Class for the Exam-page
class Exam(models.Model):
    name = models.CharField(max_length=100,default="")
    # user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(max_length=200,default="")
    option1 = models.CharField(max_length=50,default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    answer = models.CharField(max_length=50, default="",blank=True)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.question
