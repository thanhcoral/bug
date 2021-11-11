from django.shortcuts import render
from rest_framework.generics import *

from teacher.models import Teacher
from .serializer import *

# Create your views here.

class ListTeacherAPIView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
class CreateTeacherAPIView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
class UpdateTeacherAPIView(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
class DeleteTeacherAPIView(DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
class RetrieveTeacherAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

