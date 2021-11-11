from django.urls import path

from teacher import views

urlpatterns = [
    path('', views.ListTeacherAPIView.as_view()),
]
