from django.db import models

# Create your models here.
class examsolution(models.Model):
    grade  = models.IntegerField(blank = True)
    subject = models.TextField(blank = True)
    question = models.TextField(blank = True)
    answer =  models.TextField(blank = True)

    def __str__(self):
        return self.subject
        
# model for collecting question

class Ask_Qus(models.Model):

    qus = models.TextField(blank = True)

    def __str__(self):
        return self.qus
