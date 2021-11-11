from django.db import models
from django.contrib.auth.models import User

from lesson.models import Lesson

class Student(User):
    address = models.CharField(max_length=200)
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING)
