from django.urls import path
from .views import InstructorAPIView, CourseAPIView, LessonAPIView, InstructorDeleteView, InstructorUpdateView, CourseUpdateView,CourseDeleteView, LessonDeleteView, LessonUpdateView

urlpatterns = [
    path('instructors/', InstructorAPIView.as_view()),
    path('courses/', CourseAPIView.as_view()),
    path('lessons/', LessonAPIView.as_view()),
    path('instructors/<int:pk>/update/', InstructorUpdateView.as_view()),
    path('instructors/<int:pk>/delete/', InstructorDeleteView.as_view()),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view()),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view()),
    path('lessons/<int:pk>/update/', LessonUpdateView.as_view()),
    path('lessons/<int:pk>/delete/', LessonDeleteView.as_view()),
]