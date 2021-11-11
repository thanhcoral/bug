from django.shortcuts import render
from rest_framework.generics import *

from lesson.models import Lesson
from .serializer import *

# Create your views here.

class ListLessonAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
class CreateLessonAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
class UpdateLessonAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
class DeleteLessonAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
class RetrieveLessonAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

