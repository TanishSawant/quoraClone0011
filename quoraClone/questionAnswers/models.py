from django.db import models

# Create your models here.
class Questions(models.Model):
    topic = models.CharField(max_length = 50)
    question = models.TextField(blank=False, null=False, unique=True)
    timeOfAddingQuestion = models.TimeField(auto_now_add=True)
    answered = models.BooleanField(default = False)
    #_answer = models.ForeignKey(Answers)

class Answers(models.Model):
    detailed_answer = models.TextField(blank= False, null=False)
    likes = models.IntegerField(default=0)