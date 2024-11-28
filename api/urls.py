from django.urls import path
from .views import InstructorAPIView, CourseAPIView, LessonAPIView

urlpatterns = [
    path('instructor/', InstructorAPIView.as_view()),
    path('course/', CourseAPIView.as_view()),
    path('lesson/', LessonAPIView.as_view()),
]