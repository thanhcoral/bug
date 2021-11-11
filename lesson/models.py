from django.db import models

from teacher.models import Teacher
# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)