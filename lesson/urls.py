from django.urls import path

from lesson import views

urlpatterns = [
    path('', views.ListLessonAPIView.as_view()),
]
