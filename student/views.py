from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import *

from student.models import Student
from .serializer import *

from role.permisions import ViewStudentList

# Create your views here.

class StudentList(ListCreateAPIView):
    permissions_class = [ViewStudentList]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer