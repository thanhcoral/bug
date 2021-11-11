from django.urls import path

from student import views

urlpatterns = [
    path('', views.StudentList.as_view()),
]
