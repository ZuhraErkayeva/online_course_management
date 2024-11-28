from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    specialty = models.TextField()

class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='instructor')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

class Lesson(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
