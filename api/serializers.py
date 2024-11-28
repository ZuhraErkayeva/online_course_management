from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Instructor, Course, Lesson


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('id','name','email','specialty')

    def validate_email(self, obj):
        if Instructor.objects.filter(email=obj).exists():
            raise serializers.ValidationError("Bu email manzili allaqachon mavjud.")
        return obj

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'description', 'instructor', 'start_date', 'end_date')

    def validate(self, obj):
        if obj['start_date'] >= obj['end_date']:
            raise serializers.ValidationError("Kursning boshlanish sanasi tugash sanasidan oldin bo'lishi kerak.")
        return obj

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'content', 'course', 'order')

    def validate_order(self, obj):
        if obj['order'] < 1:
            raise ValidationError("Tartib raqami musbat butun son bo'lishi kerak.")
        return obj