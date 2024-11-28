from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    specialty = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='instructor')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    order = models.IntegerField()

    def __str__(self):
        return self.title
